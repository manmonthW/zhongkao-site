#!/usr/bin/env python3
"""PDF → 图片 → OCR 文本提取（物理试卷专用）

物理学科特点适配：
- 物理公式多（F=ma, P=UI, Q=cmΔt 等），OCR 后需人工校验
- 含电路图、光路图、力学示意图 → 保留原始图片便于人工查看
- 物化合卷 → 只提取物理部分（通常前 80 分）
- 实验数据表格多 → 尽量保持表格结构
"""
import fitz  # PyMuPDF
import subprocess
import sys
import os
from pathlib import Path

def pdf_to_images(pdf_path, output_dir, dpi=300):
    """将 PDF 每页转为 PNG 图片"""
    doc = fitz.open(pdf_path)
    images = []
    for i, page in enumerate(doc):
        mat = fitz.Matrix(dpi/72, dpi/72)
        pix = page.get_pixmap(matrix=mat)
        img_path = os.path.join(output_dir, f"p{i+1:02d}.png")
        pix.save(img_path)
        images.append(img_path)
        print(f"  页 {i+1}/{len(doc)} → {img_path}")
    doc.close()
    return images

def ocr_image(img_path, lang="chi_sim"):
    """对单张图片执行 OCR（中文+英文混合，适配物理公式）"""
    result = subprocess.run(
        ["tesseract", img_path, "stdout", "-l", lang, "--psm", "6"],
        capture_output=True, text=True
    )
    return result.stdout

def process_pdf(pdf_path, img_base_dir, ocr_output_path):
    """完整流程：PDF → 图片 → OCR → Markdown"""
    pdf_name = Path(pdf_path).stem
    img_dir = os.path.join(img_base_dir, pdf_name)
    os.makedirs(img_dir, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"处理: {pdf_name}")
    print(f"{'='*60}")
    
    # Step 1: PDF → 图片
    print("Step 1: PDF → 图片...")
    images = pdf_to_images(pdf_path, img_dir)
    
    # Step 2: OCR
    print("Step 2: OCR 识别...")
    all_text = []
    for img in images:
        page_num = Path(img).stem
        text = ocr_image(img)
        all_text.append(f"## 第 {page_num} 页\n\n{text}")
        print(f"  OCR {page_num}: {len(text)} 字符")
    
    # Step 3: 写入 Markdown（含物理试卷特殊标注）
    header = f"""# {pdf_name} OCR 文本

> ⚠️ 物理试卷 OCR 注意事项：
> - 物理公式（如 F=ma, P=UI, Q=cmΔt）可能 OCR 不准确，需人工校验
> - 电路图、光路图、力学示意图无法 OCR，请对照原始图片查看
> - 原始图片保存在 ocr_images/{pdf_name}/ 目录下

"""
    full_text = header + "\n\n---\n\n".join(all_text)
    with open(ocr_output_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"输出: {ocr_output_path} ({len(full_text)} 字符)")
    return full_text

if __name__ == "__main__":
    base = "/home/ekewang/projects/zhongkao/物理学科分析"
    pdf_dir = os.path.join(base, "模拟卷")
    ocr_dir = os.path.join(base, "ocr_text")
    img_base = os.path.join(base, "ocr_images")
    os.makedirs(ocr_dir, exist_ok=True)
    os.makedirs(img_base, exist_ok=True)
    
    # 如果指定了文件名参数，只处理该文件
    if len(sys.argv) > 1:
        target = sys.argv[1]
        pdfs = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) 
                if f.endswith('.pdf') and target in f]
    else:
        pdfs = sorted([os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) 
                       if f.endswith('.pdf')])
    
    if not pdfs:
        print("未找到 PDF 文件")
        sys.exit(1)
    
    print(f"共找到 {len(pdfs)} 个 PDF 文件")
    for pdf in pdfs:
        name = Path(pdf).stem
        ocr_path = os.path.join(ocr_dir, f"{name}_ocr.md")
        process_pdf(pdf, img_base, ocr_path)
    
    print(f"\n{'='*60}")
    print(f"全部完成！共处理 {len(pdfs)} 个文件")
    print(f"OCR 文本目录: {ocr_dir}")
    print(f"原始图片目录: {img_base}")
    print(f"{'='*60}")
