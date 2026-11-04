---
name: bilingual-paper-referee
version: 1.0.0
description: "Simulate rigorous peer review and journal refereeing for biomechanics papers in Persian and English, modeled after top venues such as Journal of Biomechanics, IEEE Transactions on Biomedical Engineering, and Gait & Posture. Critically assesses experimental validity, signal processing filters, soft-tissue artifacts, statistical power, and claim boundaries. Trigger when reviewing manuscripts, stress-testing thesis drafts, generating referee reports, or preparing rebuttal letters."
tools: [bash, python, read_file, write_file]
metadata:
  target_venues: [Journal-of-Biomechanics, IEEE-TBME, Gait-and-Posture, Clinical-Biomechanics, Annals-of-Biomedical-Engineering]
  languages: [fa-IR, en-US]
  role: peer-reviewer-referee
---

# Bilingual Biomechanics Paper Referee & Peer Review Engine
# موتور شبیه‌سازی داوری مقالات ژورنال‌های بیومکانیک (دوزبانه فارسی و انگلیسی)

## مأموریت (Mission)
شبیه‌سازی موشکافانه، دقیق و سازنده داوری مقالات علمی مطابق بالاترین استانداردهای ژورنال‌های معتبر مهندسی پزشکی و بیومکانیک (*Journal of Biomechanics*, *IEEE TBME*, *Gait & Posture*) برای ارزیابی پیش‌نویس مقالات، رساله‌های دکتری و پایان‌نامه‌های ارشد، جهت شناسایی ایرادات پیش از ارسال واقعی و تنظیم گزارش رسمی داوری.

---

## ابعاد پنج‌گانه ارزیابی داور (The 5-Pillar Referee Audit)

```mermaid
graph TD
    A["۱. اصالت و نوآوری علمی (Novelty & Gap)"] --> F["گزارش نهایی داوری و تصمیم‌گیری"]
    B["۲. صحت مدل بیومکانیکی (Kinematics & Kinetics)"] --> F
    C["۳. برازش پردازش سیگنال (Filtering & Cutoffs)"] --> F
    D["۴. استحکام روش‌های آماری (Power & Effect Size)"] --> F
    E["۵. انطباق ادعا با شواهد (Claim Fidelity & Limitations)"] --> F
```

### ۱. اصالت و توجیه شکاف پژوهش (Novelty & Gap)
- آیا فرضیه برآمده از یک چالش حل‌نشده بیومکانیکی است یا صرفاً تغییر جزئی پارامترهای یک مقاله قدیمی؟
- آیا ادبیات پژوهش به‌روز است و مقالات ۳ سال اخیر را پوشش می‌دهد؟

### ۲. صحت مدل‌سازی بیومکانیکی و آزمایشگاهی (Methodological Rigor)
- **ست مارکرها و مدل اسکلتی:** آیا ست مارکر (Plug-in Gait یا CAST) برای حرکت مورد نظر مناسب است؟ خطای جابه‌جایی بافت نرم (STA) چگونه کنترل یا مدل شده است؟
- **پارامترهای آنتروپومتریک:** آیا ممان اینرسی بخش‌های بدن (BSIP) بر اساس جداول معتبر محاسبه شده یا با اسکن‌های دقیق فردی؟
- **سینتیک و دینامیک معکوس:** آیا شتاب‌های زاویه‌ای و مشتق‌گیری زمانی فیلتر شده‌اند تا خطای مشتق‌گیری چندبرابر نشود؟

### ۳. پردازش سیگنال و فیلترگذاری (Signal Conditioning)
- **فرکانس قطع (Cutoff Frequency):** آیا فرکانس قطع فیلتر پایین‌گذر باترورث (مثلاً ۶ هرتز) بر اساس تحلیل باقیمانده (Residual Analysis) توجیه شده است؟
- **سینک بودن داده‌ها (Synchronization):** آیا فرکانس نمونه‌برداری موکپ (مثلاً ۱۰۰ هرتز) با صفحات نیرو (۱۰۰۰ هرتز) و EMG (۲۰۰۰ هرتز) به درستی همگام شده‌اند؟

### ۴. اعتبار تحلیل‌های آماری (Statistical Soundness)
- **حجم نمونه و توان آزمون (Power Analysis):** آیا حجم نمونه با تحلیل آماری توان (مثلاً در $G*Power$ با توان حداقل $۰٫۸۰$) تعیین شده است؟
- **آزمون نرمال بودن داده‌ها:** پیش از آزمون‌های پارامتریک، آیا نرمال بودن توزیع داده‌ها با شاپیرو-ویلک (Shapiro-Wilk) سنجیده شده است؟
- **تصحیح مقایسه‌های چندگانه:** در مقایسه عضلات یا مفاصل متعدد، آیا از تصحیح بنفرونی (Bonferroni) یا هولم استفاده شده است؟

### ۵. انطباق ادعا و بحث پیرامون محدودیت‌ها (Claim Boundaries)
- آیا نویسندگان یافته‌های حاصل از آزمودنی‌های سالم را به بیماران تعمیم داده‌اند؟
- آیا بخش صریح «محدودیت‌های پژوهش» وجود دارد؟

---

## ساختار گزارش رسمی داوری (Standard Referee Report Template)

هر گزارش داوری تولیدشده توسط این ماژول دارای ۵ بخش استاندارد است:
1. **خلاصه کلی و پیام مقاله (Summary of the Manuscript):** بیان بی‌طرفانه هدف، روش و یافته اصلی.
2. **نقاط قوت کلیدی (Key Strengths):** نوآوری، حجم داده، ابزار دقیق.
3. **ایرادات اساسی و ساختاری (Major Revisions):** نقایص متدولوژی، فیلترهای نامناسب، ابهام آماری، نتیجه‌گیری فراتر از داده‌ها.
4. **ایرادات جزئی و خط‌به‌خط (Minor Comments):** ابهامات متنی، اصلاح ارقام، واحدها، غلط‌های املایی و نشانه‌گذاری.
5. **توصیه نهایی به سرسردبیر (Recommendation to Editor):**
   - پذیرش بدون تغییر (Accept as is)
   - پذیرش با اصلاحات جزئی (Minor Revision)
   - بازنگری اساسی و داوری مجدد (Major Revision)
   - رد مقاله (Reject)
