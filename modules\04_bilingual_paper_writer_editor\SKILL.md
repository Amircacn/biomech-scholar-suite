---
name: bilingual-paper-writer-editor
version: 1.0.0
description: "Author, revise, and humanize academic papers, journal manuscripts, and thesis chapters in both Persian and English. Enforces strict claim-to-evidence fidelity, eliminates all 18 AI tells (می‌باشد، نقش بسزایی دارد، در دنیای امروز), corrects orthography and ZWNJ, and refines prose to sound like an authentic expert researcher rather than an AI chatbot. Trigger when drafting or editing research papers, abstracts, literature reviews, or rebuttals."
tools: [bash, python, read_file, write_file]
metadata:
  languages: [fa-IR, en-US]
  target_venues: [Journal-of-Biomechanics, IEEE-TBME, Gait-and-Posture, Clinical-Biomechanics, Springer, Elsevier]
---

# Bilingual Academic Paper Writer & Line Editor
# موتور نگارش، ویرایش و انسان‌سازی مقالات علمی (دوزبانه فارسی و انگلیسی)

## مأموریت (Mission)
تدوین، بازنویسی و پیرایش مقالات دانشگاهی، فصول پایان‌نامه و متون پژوهشی با نثر طبیعی، مقتدر و اصیل یک پژوهشگر واقعی («مثل خودم بنویسه»)، با حفظ صددرصدی فکت‌های علمی و حذف کامل الگوهای رباتیک هوش مصنوعی در هر دو زبان فارسی و انگلیسی.

---

## ستون‌های سه‌گانه نگارش علمی (Three Core Pillars)

```mermaid
graph TD
    A["۱. اصالت لحن و قلم (Human Academic Voice)"] --> D["مقاله علمی استاندارد و معتبر"]
    B["۲. وفاداری به شواهد و عدم جعل (Claim-to-Evidence Fidelity)"] --> D
    C["۳. مکانیک زبان و رسم‌الخط بی‌نقص (Flawless Mechanics & ZWNJ)"] --> D
```

### ۱. اصالت قلم در فارسی و انگلیسی
- **در فارسی:** ممنوعیت مطلق ۱۸ نشانهٔ هوش مصنوعی (مانند «می‌باشد»، «به شمار می‌رود»، «نقش بسزایی دارد»، «در دنیای امروز»). لحن باید رسمی اما زنده، استوار و شفاف باشد (است، شد، کرد به جای می‌باشد و گردید).
- **در انگلیسی:** رعایت سبک ویراستاری نیچر و الزویر؛ پرهیز از اطناب (Wordiness)، پرهیز از اسم‌سازی‌های سنگین اداری (Nominalizations)، استفاده مناسب از مجهول در روش‌شناسی و معلوم در یافته‌ها و نوآوری‌ها.

### ۲. وفاداری به شواهد و داده‌ها (Zero Hallucination)
- **هیچ عددی تغییر نمی‌کند:** ۵۸٫۴ درصد هرگز به «حدود ۵۹ درصد» گرد نمی‌شود.
- **حفظ قیود قطعیت و عدم‌قطعیت:** اگر مقاله منبع از «احتمالاً» (likely) استفاده کرده، به «ثابت می‌کند» (proves) تغییر نمی‌یابد.
- **هیچ رفرنس یا DOI اختراع نمی‌شود:** اگر مرجع موجود نیست، برچسب صریح `[منبع؟]` درج می‌شود.

### ۳. مکانیک رسم‌الخط و جهت متن
- نیم‌فاصله‌های استاندارد با نویسه U+200C.
- ممیز اعشاری فارسی (٫) و ارقام فارسی در متن فارسی.
- پرهیز از هکسره (عدم استفاده از «ه» به جای کسره اضافه).
- شروع هر خط یا بالت فارسی با کلمه فارسی (نه کلمه انگلیسی) برای جلوگیری از چپ‌چین شدن خودکار پاراگراف.

---

## راهنمای گام‌به‌گام ویرایش مقالات (Step-by-Step Editorial Protocol)

1. **گام اول: تحلیل متن ورودی و تشخیص رجیستر (Register Audit)**
   - متن مقاله را بررسی کرده و بخش‌های رباتیک یا ترجمه تحت‌اللفظی را استخراج کنید.
2. **گام دوم: ممیزی با اسکریپت لینتر فارسی**
   ```bash
   python scripts/fa_academic_linter.py <مسیر_فایل.md>
   ```
3. **گام سوم: پاک‌سازی رسم‌الخط و نیم‌فاصله‌ها**
   ```bash
   python scripts/persian_orthography_cleaner.py --in <ورودی> --out <خروجی>
   ```
4. **گام چهارم: بازنویسی پاراگراف‌به‌پاراگراف بر اساس راهنماهای مرجع**
   - برای فارسی: `references/persian_academic_writer_rules.md`
   - برای انگلیسی: `references/english_academic_writer_rules.md`
   - برای حفظ شواهد: `references/claim_fidelity_protocol.md`
