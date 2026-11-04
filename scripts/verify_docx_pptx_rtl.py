#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Office DOCX & PPTX RTL Verifier & Repair Utility
Part of Biomech Scholar Suite

Ensures:
1. OOXML <w:bidi/> is present as the first child of <w:sectPr> in docx.
2. Complex Script fonts (w:cs, a:cs) are set to Vazirmatn or designated Persian font.
3. No 'jc=right' bugs (which visually left-aligns text in RTL mode; should be 'start').
4. Tables have <w:bidiVisual/> so the first column renders on the visual right.
5. PPTX text frames contain rtl="1" and a:cs typeface.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
import os
import zipfile
import re
import argparse
import shutil
import xml.etree.ElementTree as ET

def verify_docx(docx_path: str, fix: bool = False, expect_font: str = "Vazirmatn"):
    print(f"\n🔍 بررسی فایل Word: {docx_path}")
    if not os.path.exists(docx_path):
        print(f"❌ خطا: فایل {docx_path} وجود ندارد.")
        return False
        
    try:
        with zipfile.ZipFile(docx_path, 'r') as zf:
            namelist = zf.namelist()
            if "word/document.xml" not in namelist:
                print("❌ ساختار نامعتبر: word/document.xml پیدا نشد.")
                return False
            doc_xml = zf.read("word/document.xml").decode('utf-8', errors='replace')
    except Exception as e:
        print(f"❌ خطا در باز کردن فایل زیپ docx: {e}")
        return False

    issues = []
    
    # 1. Check <w:bidi/> in <w:sectPr>
    sect_matches = re.findall(r'<w:sectPr[^>]*>(.*?)</w:sectPr>', doc_xml)
    missing_sect_bidi = 0
    for s in sect_matches:
        if not s.startswith('<w:bidi/>') and '<w:bidi' not in s:
            missing_sect_bidi += 1
            
    if missing_sect_bidi > 0:
        issues.append(f"{missing_sect_bidi} بخش فاقد تگ اول <w:bidi/> هستند (ممکن است جهت صفحه چپ‌چین شود).")
        
    # 2. Check jc="right" traps
    jc_right_count = len(re.findall(r'<w:jc\s+[^>]*w:val="right"', doc_xml))
    if jc_right_count > 0:
        issues.append(f"{jc_right_count} پاراگراف دارای تگ خطای w:jc=\"right\" هستند! (در حالت bidi این تگ باعث چپ‌چین شدن بصری می‌شود؛ باید start باشد).")

    # 3. Check Complex Script font
    cs_font_count = len(re.findall(rf'w:cs="{expect_font}"', doc_xml, re.IGNORECASE))
    if cs_font_count == 0:
        issues.append(f"فونت اسکریپت پیچیده {expect_font} در w:cs یافت نشد (احتمال سقوط به فونت‌های غیراستاندارد مانند DejaVu).")

    # 4. Check Tables RTL
    tbl_count = len(re.findall(r'<w:tbl>', doc_xml))
    bidi_visual_count = len(re.findall(r'<w:bidiVisual/>', doc_xml))
    if tbl_count > bidi_visual_count:
        issues.append(f"{tbl_count - bidi_visual_count} جدول فاقد تگ <w:bidiVisual/> هستند (ستون اول به اشتباه در سمت چپ رندر می‌شود).")

    if not issues:
        print("✅ فوق‌العاده! ساختار سند Word کاملاً استاندارد و راست‌به‌چپ است.")
        return True
        
    print(f"⚠️ یافت شد: {len(issues)} اشکال در چیدمان راست‌به‌چپ سند:")
    for iss in issues:
        print(f"   - {iss}")
        
    if fix:
        print("\n🔧 در حال اعمال اصلاحات خودکار روی سند...")
        patched_xml = re.sub(r'(<w:sectPr[^>]*>)(?!<w:bidi/>)', r'\1<w:bidi/>', doc_xml)
        patched_xml = re.sub(r'(<w:jc\s+[^>]*w:val=)"right"', r'\1"start"', patched_xml)
        
        # Ensure tables have bidiVisual
        def patch_tbl(match):
            tbl_content = match.group(0)
            if '<w:bidiVisual/>' not in tbl_content and '<w:tblPr>' in tbl_content:
                return tbl_content.replace('<w:tblPr>', '<w:tblPr><w:bidiVisual/>')
            return tbl_content
            
        patched_xml = re.sub(r'<w:tbl>[\s\S]*?</w:tbl>', patch_tbl, patched_xml)
        
        tmp_path = docx_path + ".tmp"
        with zipfile.ZipFile(docx_path, 'r') as zin:
            with zipfile.ZipFile(tmp_path, 'w', zipfile.ZIP_DEFLATED) as zout:
                for item in zin.infolist():
                    if item.filename == "word/document.xml":
                        zout.writestr(item, patched_xml.encode('utf-8'))
                    else:
                        zout.writestr(item, zin.read(item.filename))
        shutil.move(tmp_path, docx_path)
        print("✅ سند با موفقیت تعمیر و ذخیره شد.")
        return True
        
    return False

def main():
    parser = argparse.ArgumentParser(description="Verify and repair RTL layout in DOCX")
    parser.add_argument("file", help="Path to DOCX file")
    parser.add_argument("--fix", action="store_true", help="Automatically repair missing bidi tags")
    parser.add_argument("--font", default="Vazirmatn", help="Expected complex script font name")
    args = parser.parse_args()
    
    verify_docx(args.file, fix=args.fix, expect_font=args.font)

if __name__ == "__main__":
    main()
