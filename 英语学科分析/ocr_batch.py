#!/usr/bin/env python3
"""Batch OCR all English exam PDFs."""

import fitz  # PyMuPDF
import subprocess, os, sys

BASE = "/mnt/c/Users/ekewang/OneDrive - Ericsson/B-Work/AI/中考模拟"
OUT = "/home/ekewang/projects/zhongkao/英语学科分析/ocr_text"

EXAMS = [
    # (prefix, pdf_path, is_answer)
    ("沈河区一模", "2026年沈阳沈河区一模/2026.4沈阳沈河区九下一模-英语.pdf", False),
    ("沈河区一模", "2026年沈阳沈河区一模/2026辽宁沈阳沈河区九下一模英语含答案.pdf", True),
    ("于洪区一模", "2026年4月于洪区区模/2026年沈阳市于洪区一模英语试卷.pdf", False),
    ("于洪区一模", "2026年4月于洪区区模/沈阳于洪区2025-2026学年九年级中考一模英语试卷+答案.pdf", True),
    ("浑南区一模", "沈阳浑南区/2026年4月沈阳浑南英语一模_.pdf", False),
    ("浑南区一模", "沈阳浑南区/2026年4月沈阳浑南英语一模答案_.pdf", True),
    ("皇姑区一模", "沈阳皇姑区/2026年皇姑区一模英语.pdf", False),
    ("皇姑区一模", "沈阳皇姑区/2026年皇姑区一模英语答案.pdf", True),
    ("苏家屯区一模", "沈阳苏家屯区/辽宁沈阳市苏家屯区2025-2026学年九年级下 中考一模英语试题.pdf", False),
    ("苏家屯区一模", "沈阳苏家屯区/沈阳苏家屯2025-2026学年九年级中考一模英语试卷答案.pdf", True),
    ("铁西区一模", "沈阳铁西区/2026铁西区一模英语试卷.pdf", False),
    ("铁西区一模", "沈阳铁西区/2026铁西区一模英语试卷答案.pdf", True),
    ("抚顺一模", "抚顺一模/2026.4.20辽宁抚顺市统考英语试卷.pdf", False),
    ("抚顺一模", "抚顺一模/英语答案 2026年抚顺市初中学业水平模拟考试英语.pdf", True),
    ("营口市一模", "营口市一模/2026年4月营口市市一模英语试卷.pdf", False),
    ("铁岭二模", "铁岭二模/2026.4铁岭九年英语二模试卷+答案.pdf", False),  # combined
]

def ocr_pdf(pdf_path, out_md):
    """Convert PDF to images, OCR each page, write markdown."""
    doc = fitz.open(pdf_path)
    pages_text = []
    for i, page in enumerate(doc):
        mat = fitz.Matrix(300/72, 300/72)
        pix = page.get_pixmap(matrix=mat)
        img_path = f"/tmp/eng_ocr_p{i:02d}.png"
        pix.save(img_path)
        result = subprocess.run(
            ["tesseract", img_path, "stdout", "-l", "eng+chi_sim", "--psm", "6"],
            capture_output=True, text=True
        )
        pages_text.append(f"## 第 p{i+1:02d} 页\n\n{result.stdout.strip()}")
        os.remove(img_path)
    doc.close()
    
    basename = os.path.basename(pdf_path)
    with open(out_md, "w", encoding="utf-8") as f:
        f.write(f"# {basename} OCR 文本\n\n")
        f.write("\n\n---\n\n".join(pages_text))
        f.write("\n")
    print(f"  ✓ {out_md} ({len(pages_text)} pages)")

os.makedirs(OUT, exist_ok=True)

for prefix, rel_path, is_answer in EXAMS:
    pdf_path = os.path.join(BASE, rel_path)
    suffix = "答案" if is_answer else "试卷"
    out_md = os.path.join(OUT, f"{prefix}_英语{suffix}_ocr.md")
    
    if os.path.exists(out_md):
        print(f"  ⏭ Skip (exists): {out_md}")
        continue
    
    if not os.path.exists(pdf_path):
        print(f"  ✗ Not found: {pdf_path}")
        continue
    
    print(f"Processing: {prefix} ({suffix})...")
    try:
        ocr_pdf(pdf_path, out_md)
    except Exception as e:
        print(f"  ✗ Error: {e}")
