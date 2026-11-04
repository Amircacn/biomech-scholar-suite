---
name: bilingual-academic-pptx
version: 1.0.0
description: "Design and build high-impact bilingual academic presentations for biomechanics conferences (10-15 min), master thesis defenses (40-45 min), seminar lectures, and lab meetings in PowerPoint (.pptx) and LaTeX Beamer. Trigger when creating or editing research slides, defense presentations, conference decks, or fixing Persian RTL PowerPoint formatting."
tools: [bash, python, read_file, write_file]
metadata:
  formats: [pptx, beamer, marp]
  languages: [fa-IR, en-US]
  domain: academic-presentations
---

# Bilingual Academic Presentation Engine
# موتور ارائه‌های آکادمیک و دفاع پایان‌نامه بیومکانیک

## مأموریت (Mission)
طراحی، اسکلت‌بندی و تولید ارائه‌های علمی درجه‌یک برای کنفرانس‌های ملی و بین‌المللی، جلسات دفاع پایان‌نامه کارشناسی ارشد و دکتری بیومکانیک، سمینارها و جلسات گزارش پیشرفت به استاد راهنما، با چیدمان دیداری بهینه و حل کامل چالش‌های راست‌به‌چپ (RTL) در مایکروسافت پاورپوینت (`.pptx`).

---

## ۳ آرکی‌تایپ اصلی ارائه (3 Core Presentation Archetypes)

| ردیف | نوع ارائه | زمان استاندارد | تعداد اسلاید | تمرکز محتوایی |
|---|---|---|---|---|
| ۱ | **ارائه مقاله کنفرانس** (Conference Talk) | ۱۰ تا ۱۲ دقیقه (+ ۳ دقیقه پرسش) | ۸ تا ۱۲ اسلاید | مسئله مشخص، نوآوری روش، یافته‌های کلیدی در ۲ نمودار، نتیجه کاربردی |
| ۲ | **جلسه دفاع پایان‌نامه** (Thesis Defense) | ۳۵ تا ۴۵ دقیقه | ۳۰ تا ۴۰ اسلاید | مرور جامع شکاف پژوهش، روش‌شناسی دقیق، اعتبارسنجی تجربی، تحلیل حساسیت، دستاوردها و محدودیت‌ها |
| ۳ | **جلسه هفتگی آزمایشگاه** (Lab Progress Meeting) | ۱۵ تا ۲۰ دقیقه | ۱۰ تا ۱۵ اسلاید | کارهای انجام‌شده هفته گذشته، موانع فنی/پردازشی، داده‌های تازه، اهداف هفته بعد |

---

## اصول طراحی اسلایدهای علمی (Academic Slide Design Principles)

1. **قانون یک پیام در هر اسلاید (One Core Takeaway per Slide):**
   - عنوان اسلاید نباید صرفاً یک عبارت خنثی مانند «روش‌شناسی» باشد؛ عنوان باید ادعای اصلی اسلاید را بیان کند:
     - ❌ `نتایج آزمایشگاهی`
     - ✅ `افزایش ۲۰ درصدی گشتاور اکستنشن زانو با استفاده از ارتز تطبیقی`
2. **چگالی بصری بالا در برابر گلوله‌نقطه‌ها (High Visual Density over Bullet Points):**
   - از دیوارهای متنی پرهیز کنید. مخاطب یا اسلاید را می‌خواند یا به صحبت‌های شما گوش می‌دهد.
   - چیدمان دوبخشی: نمودار یا تصویر سه‌بعدی متحرک در یک سو (راست برای فارسی، چپ برای انگلیسی)، ۲ تا ۳ گزاره عددی برجسته در سوی دیگر.
3. **آیینه‌سازی چیدمان در اسلایدهای فارسی (RTL Layout Mirroring):**
   - چشم خواننده فارسی‌زبان از گوشه بالا-راست وارد اسلاید می‌شود. بنابراین:
     - عنوان در بالا سمت راست (یا مرکز).
     - بخش اصلی محتوا در سمت راست، تصویر/نمودار توضیحی در سمت چپ.
     - بردارهای فرآیندی و فلش‌های زمانی از راست به چپ جریان می‌یابند ($\leftarrow$).

---

## قوانین فنی پاورپوینت فارسی با `python-pptx`

پاورپوینت سوئیچ سراسری RTL ندارد و جهت باید روی تک‌تک پاراگراف‌ها و متن‌ها تنظیم شود:
1. **جهت پاراگراف:** اعمال `pPr.set('rtl', '1')` و تراز فیزیکی `PP_ALIGN.RIGHT` (در زبان DrawingML برعکس Word، تراز R نشان‌دهنده راست فیزیکی است).
2. **فونت اسکریپت پیچیده (Complex Script):** اضافه کردن تگ `a:cs` با فونت `Vazirmatn`:
   ```python
   cs = rPr.find(qn('a:cs'))
   if cs is None: cs = etree.SubElement(rPr, qn('a:cs'))
   cs.set('typeface', 'Vazirmatn')
   ```
3. **اعداد فارسی:** شماره اسلایدها و لیست‌های نقطه‌ای با ارقام فارسی (`۱. `، `۲. `) تنظیم شوند تا جهت خط معکوس نشود.
4. **اعتبارسنجی:** فایل خروجی را با `python scripts/verify_docx_pptx_rtl.py` بازبینی کنید.
