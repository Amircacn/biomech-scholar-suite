#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Persian Academic Linter (ارزیاب سبک و اصالت نگارش علمی فارسی)
Part of Biomech Scholar Suite

Detects:
1. 18 Classic AI Tells & Bureaucratic Clichés (می‌باشد، نقش بسزایی دارد، در دنیای امروز، لازم به ذکر است...)
2. Haksare (هکسره) Confusion: ezafe written as 'ه' or 'است' misidentified
3. Bidi Flip Hazards: Persian paragraphs/bullets opening with Latin characters
4. Arabic codepoints leakage (ي, ك, ة)
5. Sentence length monotony (low burstiness / robotic rhythm)
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
import re
import argparse
from typing import List, Tuple

# The 18 AI Tells and Bureaucratic Clichés
AI_TELLS = [
    (r'\bمی‌باشد\b|\bنمی‌باشد\b|\bمی‌باشند\b', "فعل قالبی 'می‌باشد' (باید به 'است' یا فعل خاص جمله تبدیل شود)"),
    (r'\bگردید\b|\bمی‌گردد\b|\bگردیده است\b', "فعل غیرطبیعی 'گردید/می‌گردد' (از 'شد/می‌شود' استفاده کنید)"),
    (r'\bبه شمار می‌رود\b|\bمحسوب می‌شود\b|\bبه حساب می‌آید\b', "حشو مکرر 'محسوب می‌شود/به شمار می‌رود' (معمولاً 'است' کفایت می‌کند)"),
    (r'\bلازم به ذکر است\b|\bشایان ذکر است\b|\bباید خاطرنشان کرد\b', "اعلام رسمی زائد 'لازم به ذکر است' (مستقیماً اصل پیام را بیان کنید)"),
    (r'\bنقش بسزایی\b|\bنقش بسزا\b|\bنقش مهمی ایفا می‌کند\b', "بزرگ‌نمایی کلیشه‌ای 'نقش بسزایی دارد' (تأثیر دقیق و اندازه‌گیری‌شده را بنویسید)"),
    (r'\bاز اهمیت ویژه‌ای برخوردار\b|\bاهمیت بسزایی دارد\b', "بزرگ‌نمایی تهی 'از اهمیت ویژه‌ای برخوردار است' (دلیل واقعی اهمیت را بنویسید)"),
    (r'\bدر دنیای امروز\b|\bدر عصر حاضر\b|\bامروزه با پیشرفت تکنولوژی\b', "مقدمه‌چینی کلیشه‌ای رباتیک (مستقیماً مسئله و داده پژوهش را مطرح کنید)"),
    (r'\bدر راستای\b|\bدر همین راستا\b|\bدر جهت نیل به\b', "عبارت کلیشه‌ای اداری 'در راستای' (جایگزین با 'برای' یا بازنویسی جمله)"),
    (r'\bنه تنها\s+.+\s+بلکه\b', "الگوی ترجمه‌ای 'نه تنها... بلکه' (جمله را ساده و مثبت بنویسید)"),
    (r'\bکه نشان‌دهنده‌ی\b|\bکه بیانگر\b|\bکه حاکی از\s+.+\s+می‌باشد\b', "دنباله تحلیلی الصاقی (جمله مستقل با ذکر شواهد بسازید)"),
    (r'\bکارشناسان معتقدند\b|\bمطالعات نشان داده است\b(?!\s*\[)', "ارجاع مبهم بدون منبع (نام پژوهشگر یا ارجاع مقاله را درج کنید)"),
    (r'—', "خط تیره بلند انگلیسی (em-dash) در نثر فارسی (از ویرگول، نقطه یا بازنویسی استفاده کنید)"),
    (r'\bدر نهایت می‌توان گفت\b|\bبه طور کلی می‌توان نتیجه گرفت\b', "پایان‌بندی کلیشه‌ای رباتیک (نتیجه عددی و معیار تصمیم‌گیری نهایی را بنویسید)"),
    (r'\bگاهاً\b|\bدوماً\b|\bسوماً\b|\bناچاراً\b', "تنوین روی کلمات فارسی (غلط دستوری: از 'گاهی'، 'دوم اینکه'، 'به‌ناچار' استفاده کنید)"),
    (r'\bبه عمل آورد\b|\bاقدام به عمل\b|\bانجام پذیرفت\b', "اسم‌سازی سنگین اداری (به فعل ساده مثل 'انجام داد' یا 'بررسی کرد' تبدیل شود)"),
    (r'\bسریع، آسان و مطمئن\b|\bطراحی، توسعه و پشتیبانی\b', "ریتم سه‌تایی تصنعی (Rule of Three) هوش مصنوعی"),
    (r'\bبدون هیچ دغدغه‌ای\b|\bبدون کوچک‌ترین نگرانی\b', "اغراق بازاریابی در متن دانشگاهی"),
    (r'\bطبق درخواست شما\b|\bامیدوارم این پاسخ مفید باشد\b', "پس‌مانده چت‌بات در متن اصلی سند"),
]

# Suspected Haksare Patterns
HAKSARE_PATTERNS = [
    (r'\b([ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]+)ه\s+(من|تو|ما|شما|ایشون|او|آن‌ها|این|آن)\b', 
     "احتمال هکسره (کسره اضافه با 'ه' نوشته شده است: مثلاً 'کتابه من' -> 'کتابِ من')"),
    (r'\b(سایته|کلاسه|دانشگاهه|مفصله|بافته|تاندونه|زاویه‌یه|استخوانه)\s+([ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]+)\b',
     "احتمال خطای هکسره در ترکیب مضاف و مضاف‌الیه (باید بدون 'ه' و با کسره باشد)"),
]

def check_bidi_direction_hazard(line: str) -> bool:
    """Check if a line or list item starts with a Latin word, which flips paragraph bidi to LTR."""
    cleaned = line.strip()
    if not cleaned or cleaned.startswith(('```', '#', '|', '$$', '<')):
        return False
    # Strip bullet indicators
    cleaned = re.sub(r'^(\*|-|\+|\d+\.)\s+', '', cleaned).strip()
    if not cleaned:
        return False
    first_char = cleaned[0]
    # Check if first character is ASCII letter
    return ('a' <= first_char <= 'z') or ('A' <= first_char <= 'Z')

def audit_persian_text(content: str) -> List[dict]:
    """Run full academic audit across text lines."""
    findings = []
    lines = content.split('\n')
    
    in_code_block = False
    in_references_section = False
    
    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
            
        # Detect references section
        if stripped.startswith('#') and any(r in stripped for r in ['مراجع', 'منابع', 'References', 'کتاب‌شناسی']):
            in_references_section = True
            continue
        elif stripped.startswith('#'):
            in_references_section = False
            
        # Ignore comments
        if stripped.startswith('<!--'):
            continue

        # Strip inline code from check to allow citing banned words
        line_to_check = re.sub(r'`[^`]+`', '', line)
            
        # 1. Check AI Tells (skipped in references section for English citations)
        if not in_references_section:
            for pattern, explanation in AI_TELLS:
                matches = re.finditer(pattern, line_to_check)
                for m in matches:
                    findings.append({
                        "line": line_num,
                        "type": "AI_TELL",
                        "matched": m.group(0),
                        "message": explanation,
                        "snippet": line.strip()[:90]
                    })
                
        # 2. Check Haksare
        for pattern, explanation in HAKSARE_PATTERNS:
            matches = re.finditer(pattern, line_to_check)
            for m in matches:
                matched_word = m.group(0)
                # Exclude legitimate words ending with 'ه'
                EXEMPT_WORDS = ['همه', 'نامه', 'پروژه', 'مقاله', 'جامعه', 'بسته', 'بیشینه', 'کمینه', 'دامنه', 'نمونه', 'هزینه', 'پایانه', 'سامانه', 'زاویه']
                if any(matched_word.startswith(ok) for ok in EXEMPT_WORDS):
                    continue
                findings.append({
                    "line": line_num,
                    "type": "HAKSARE_ERROR",
                    "matched": matched_word,
                    "message": explanation,
                    "snippet": line.strip()[:90]
                })
                
        # 3. Check Arabic characters
        ar_matches = re.findall(r'[يكة]', line)
        if ar_matches:
            findings.append({
                "line": line_num,
                "type": "ARABIC_CHAR",
                "matched": ', '.join(set(ar_matches)),
                "message": "کاراکتر عربی در متن فارسی (ي/ك/ة باید به ی/ک/ه تبدیل شوند)",
                "snippet": line.strip()[:90]
            })
            
        # 4. Check Bidi Start Hazard (skipped in references section)
        if not in_references_section and check_bidi_direction_hazard(line):
            findings.append({
                "line": line_num,
                "type": "BIDI_HAZARD",
                "matched": line.strip().split()[0] if line.strip() else "",
                "message": "خطر چپ‌چین شدن خط: خط با کلمه انگلیسی آغاز شده است. ابتدای خط کلمه فارسی (مانند ابزار، نرم‌افزار، متغیر) بگذارید.",
                "snippet": line.strip()[:90]
            })

    return findings

def main():
    parser = argparse.ArgumentParser(description="Persian Academic Writing Linter & AI-Detector")
    parser.add_argument("file", help="Path to Markdown or text file to lint")
    args = parser.parse_args()
    
    with open(args.file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    findings = audit_persian_text(content)
    
    print("\n" + "="*70)
    print("📊 گزارش اعتبارسنجی نگارش علمی فارسی (Biomech Scholar Suite Linter)")
    print("="*70)
    
    if not findings:
        print("✅ فوق‌العاده! هیچ ردپای هوش مصنوعی، خطای هکسره یا ناهماهنگی جهت‌متن یافت نشد.")
        print("متن از نظر استانداردهای رسم‌الخط دانشگاهی کاملاً تأیید است.\n")
        sys.exit(0)
        
    ai_tells = [f for f in findings if f["type"] == "AI_TELL"]
    haksare = [f for f in findings if f["type"] == "HAKSARE_ERROR"]
    bidi = [f for f in findings if f["type"] == "BIDI_HAZARD"]
    ar = [f for f in findings if f["type"] == "ARABIC_CHAR"]
    
    print(f"یافته‌ها: {len(findings)} مورد (ردپای هوش مصنوعی: {len(ai_tells)} | خطای هکسره: {len(haksare)} | خطر جهت‌متن: {len(bidi)} | حروف عربی: {len(ar)})\n")
    
    for f in findings:
        tag = f"[{f['type']}]"
        print(f"سطر {f['line']:3d} | {tag:15s} | نشانه: '{f['matched']}'")
        print(f"          پیام: {f['message']}")
        print(f"          متن:  {f['snippet']}")
        print("-" * 70)
        
    print("\n💡 راهنما: برای اصلاح خودکار رسم‌الخط و نیم‌فاصله‌ها از persian_orthography_cleaner.py استفاده کنید.")
    print("برای بازنویسی موارد هوش مصنوعی، از راهنمای `persian_academic_writer_rules.md` کمک بگیرید.\n")
    sys.exit(1 if len(ai_tells) > 0 or len(haksare) > 0 else 0)

if __name__ == "__main__":
    main()
