#!/usr/bin/env python3
"""PDF → 图片 → OCR 文本提取（化学试卷专用）"""
import fitz
import subprocess
import sys
import os
from pathlib import Path

def pdf_to_images(pdf_path, output_dir, dpi=300):
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
    result = subprocess.run(
        ["tesseract", img_path, "stdout", "-l", lang, "--psm", "6"],
        capture_output=True, text=True
    )
    return result.stdout

def process_pdf(pdf_path, output_dir, ocr_output_path):
    pdf_name = Path(pdf_path).stem
    img_dir = os.path.join(output_dir, "images", pdf_name)
    os.makedirs(img_dir, exist_ok=True)
    print(f"\n{'='*60}")
    print(f"处理: {pdf_name}")
    print(f"{'='*60}")
    print("Step 1: PDF → 图片...")
    images = pdf_to_images(pdf_path, img_dir)
    print("Step 2: OCR 识别...")
    all_text = []
    for img in images:
        page_num = Path(img).stem
        text = ocr_image(img)
        all_text.append(f"## 第 {page_num} 页\n\n{text}")
        print(f"  OCR {page_num}: {len(text)} 字符")
    full_text = f"# {pdf_name} OCR 文本\n\n" + "\n\n---\n\n".join(all_text)
    with open(ocr_output_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"输出: {ocr_output_path} ({len(full_text)} 字符)")
    return full_text

if __name__ == "__main__":
    base = "/home/ekewang/projects/zhongkao/化学学科分析"
    pdf_dir = os.path.join(base, "模拟卷")
    ocr_dir = os.path.join(base, "ocr_text")
    img_base = os.path.join(base, "ocr_images")
    os.makedirs(ocr_dir, exist_ok=True)
    os.makedirs(img_base, exist_ok=True)
    if len(sys.argv) > 1:
        target = sys.argv[1]
        pdfs = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith('.pdf') and target in f]
    else:
        pdfs = sorted([os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith('.pdf')])
    for pdf in pdfs:
        name = Path(pdf).stem
        ocr_path = os.path.join(ocr_dir, f"{name}_ocr.md")
        process_pdf(pdf, img_base, ocr_path)
    print(f"\n✅ 全部完成，共处理 {len(pdfs)} 个 PDF")
