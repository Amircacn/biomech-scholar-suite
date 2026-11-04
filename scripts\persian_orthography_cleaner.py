#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Persian Orthography & Mechanics Cleaner (پاک‌ساز رسم‌الخط و مکانیک متن فارسی)
Part of Biomech Scholar Suite (مجموعه جامع پژوهشی و آکادمیک بیومکانیک)

Features:
- ZWNJ (نیم‌فاصله) correction for verbs, plurals, comparatives, prefixes.
- Arabic character normalization (ي -> ی, ك -> ک, ة -> ه/ت).
- Persian digits conversion in running Persian text (leaving code/math/URLs intact).
- Punctuation spacing (، ؛ ؟ « » : . !) and guillemets replacement.
- Safe markdown parsing: protects fenced code blocks, inline code, LaTeX math, and URLs.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
import re
import argparse

# Persian and English Digits mapping
EN_DIGITS = "0123456789"
FA_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
AR_DIGITS = "٠١٢٣٤٥٦٧٨٩"

EN_TO_FA_DIGIT_MAP = str.maketrans(EN_DIGITS, FA_DIGITS)
AR_TO_FA_DIGIT_MAP = str.maketrans(AR_DIGITS, FA_DIGITS)

ZWNJ = "\u200c"

def normalize_persian_characters(text: str) -> str:
    """Normalize Arabic characters to standard Persian characters."""
    replacements = {
        'ي': 'ی',
        'ك': 'ک',
        'ى': 'ی',
        'ئ': 'ئ',
        'ؤ': 'ؤ',
        'أ': 'ا',
        'إ': 'ا',
        'ة': 'ه',
    }
    for ar_char, fa_char in replacements.items():
        text = text.replace(ar_char, fa_char)
    return text

def fix_zwnj_patterns(text: str) -> str:
    """Correct ZWNJ (نیم‌فاصله) for Persian affixes, prefixes, and compounds."""
    # Prefix می and نمی followed by verb
    text = re.sub(r'(^|\s)(ن?می)\s+([ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی])', r'\1\2' + ZWNJ + r'\3', text)
    
    # Plural 'ها'
    text = re.sub(r'([ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی])\s+(ها|های|هایم|هایت|هایش|هایمان|هایتان|هایشان)\b', r'\1' + ZWNJ + r'\2', text)
    
    # Comparative 'تر' and 'ترین'
    text = re.sub(r'([ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی])\s+(تر|ترین|تری)\b', r'\1' + ZWNJ + r'\2', text)
    
    # Suffix 'ام', 'ات', 'اش', 'ای' after 'ه'
    text = re.sub(r'([ه])\s+(ام|ات|اش|ای|اید|ایم|اند)\b', r'\1' + ZWNJ + r'\2', text)
    
    # Prefix 'بی'
    text = re.sub(r'\b(بی)\s+([ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی])', r'\1' + ZWNJ + r'\2', text)
    
    # Compound prepositions: به‌سمت، به‌صورت، به‌دلیل
    text = re.sub(r'\b(به)\s+(سمت|صورت|دلیل|عنوان|طور|ویژه|راحتی|خوبی|سرعت|تدریج)\b', r'\1' + ZWNJ + r'\2', text)
    
    return text

def fix_punctuation_and_quotes(text: str) -> str:
    """Standardize Persian punctuation and replace English quotes with guillemets."""
    # Replace English quotes with Persian guillemets
    text = re.sub(r'"([^"\n]+)"', r'«\1»', text)
    text = re.sub(r'“([^”\n]+)”', r'«\1»', text)
    
    # Standardize Persian punctuation marks
    text = text.replace('?', '؟')
    text = text.replace(';', '؛')
    text = re.sub(r'(?<![0-9]),(?![0-9])', '،', text)
    
    # Spacing around punctuation: no space before, one space after
    text = re.sub(r'\s+([،؛؟:.!])', r'\1', text)
    text = re.sub(r'([،؛؟:.!])(?=[^\s،؛؟:.!«»\)"\]\}0-9])', r'\1 ', text)
    
    # Guillemet spacing: outer space, inner no space
    text = re.sub(r'«\s+', '«', text)
    text = re.sub(r'\s+»', '»', text)
    
    # Remove excessive repetitive punctuation (e.g. !!! or ????)
    text = re.sub(r'!{2,}', '!', text)
    text = re.sub(r'؟{2,}', '؟', text)
    
    return text

def convert_digits_in_persian_context(text: str) -> str:
    """Convert digits to Persian digits when surrounded by Persian words, preserving Latin numbers."""
    text = text.translate(AR_TO_FA_DIGIT_MAP)
    
    # Replace digits preceded or followed by Persian characters
    fa_char_class = r'[\u0600-\u06FF]'
    
    def replace_digit_match(match):
        return match.group(0).translate(EN_TO_FA_DIGIT_MAP)
    
    # Pattern: digits attached to or neighboring Persian words or units (درصد, متر, نیوتن, ثانیه)
    pattern = rf'({fa_char_class}+\s*)(\d+)|(\d+)(\s*{fa_char_class}+)'
    
    # Repeat replacement for clustered numbers
    for _ in range(2):
        text = re.sub(pattern, replace_digit_match, text)
        
    return text

def process_markdown_text(content: str) -> str:
    """Extract code blocks, math expressions, and markdown links, then clean Persian prose safely."""
    placeholders = []
    
    def save_placeholder(match):
        placeholders.append(match.group(0))
        return f"__SAFE_PROTECTED_BLOCK_{len(placeholders)-1}__"

    # 1. Protect fenced code blocks ``` ... ```
    content = re.sub(r'```[\s\S]*?```', save_placeholder, content)
    
    # 2. Protect inline code ` ... `
    content = re.sub(r'`[^`\n]+`', save_placeholder, content)
    
    # 3. Protect display math $$ ... $$ and inline math $ ... $
    content = re.sub(r'\$\$[\s\S]*?\$\$', save_placeholder, content)
    content = re.sub(r'\$[^$\n]+\$', save_placeholder, content)
    
    # 4. Protect URLs and Markdown link targets
    content = re.sub(r'https?://[^\s\)]+', save_placeholder, content)
    
    # Process prose
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            # Table row: preserve formatting structure, clean individual cells
            cells = line.split('|')
            cleaned_cells = []
            for cell in cells:
                c = normalize_persian_characters(cell)
                c = fix_zwnj_patterns(c)
                c = fix_punctuation_and_quotes(c)
                cleaned_cells.append(c)
            cleaned_lines.append('|'.join(cleaned_cells))
        else:
            line_clean = normalize_persian_characters(line)
            line_clean = fix_zwnj_patterns(line_clean)
            line_clean = fix_punctuation_and_quotes(line_clean)
            line_clean = convert_digits_in_persian_context(line_clean)
            cleaned_lines.append(line_clean)
            
    result = '\n'.join(cleaned_lines)
    
    # Restore protected blocks
    for i, original in enumerate(placeholders):
        result = result.replace(f"__SAFE_PROTECTED_BLOCK_{i}__", original)
        
    return result

def main():
    parser = argparse.ArgumentParser(description="Persian Academic Orthography & ZWNJ Cleaner")
    parser.add_argument("--in", dest="input_file", required=True, help="Input text or markdown file")
    parser.add_argument("--out", dest="output_file", required=False, help="Output file (defaults to overwrite input)")
    args = parser.parse_args()
    
    out_path = args.output_file if args.output_file else args.input_file
    
    with open(args.input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()
        
    cleaned = process_markdown_text(raw_text)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)
        
    print(f"✅ Successfully cleaned Persian orthography: '{args.input_file}' -> '{out_path}'")

if __name__ == "__main__":
    main()
