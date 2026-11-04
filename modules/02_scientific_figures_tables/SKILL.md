---
name: scientific-figures-tables
version: 1.0.0
description: "Generate publication-grade scientific plots, charts, and 3-rule academic tables (APA 7th & IEEE compliant) for biomechanics papers, lab reports, and thesis defense presentations in Persian and English. Trigger when plotting gait cycles, EMG envelopes, stress-strain curves, or formatting academic tables."
tools: [bash, python, read_file, write_file]
metadata:
  domain: data-visualization
  standards: [APA-7th, IEEE, Nature-Guidelines, Okabe-Ito-Colorblind]
---

# Scientific Figures & Publication Tables Engine
# موتور تولید نمودارهای برداری و جداول استاندارد علمی

## مأموریت (Mission)
ایجاد نمودارهای داده‌محور تکرارپذیر، برداری (PDF/SVG) و رستر با وضوح بالا (300+ DPI)، همراه با جداول ۳ خطی استاندارد علمی به هر دو زبان فارسی و انگلیسی، منطبق بر ضوابط انتشارات معتبر بیومکانیک (Elsevier, IEEE, Springer, Nature).

---

## اصول طراحی نمودار علمی (Scientific Plotting Rules)

1. **پالت رنگی استاندارد دانشگاهی (Okabe-Ito Palette):**
   - آبی خلبانی: `#0072B2`
   - نارنجی ملایم: `#E69F00`
   - سبز تیره: `#009E73`
   - قرمز شرابی (ورمیلیون): `#D55E00`
   - بنفش زنگاری: `#CC79A7`
   - این پالت برای افراد مبتلا به کوررنگی کاملاً تفکیک‌پذیر بوده و در چاپ سیاه‌وسفید نیز تداخل نوری ندارد.
2. **برچسب‌گذاری محورها با واحد در کروشه:**
   - زوایا: `Knee Flexion (+) / Extension (-) [deg]` یا `زاویه فلکشن (+) / اکستنشن (-) زانو [درجه]`
   - نیروها: `Vertical Ground Reaction Force Fz [BW]` یا `نیروی عمودی زمین [BW]`
   - گشتاور: `Net Internal Extension Moment [N·m/kg]` یا `گشتاور داخلی اکستنشن [N·m/kg]`
3. **حذف خطوط کادر زائد (Despine):**
   - خطوط کادر بالا (Top Spine) و راست (Right Spine) همواره باید حذف شوند.
   - جهت تیک‌های محور (Tick Direction) رو به داخل (`direction='in'`).
4. **نمایش عدم قطعیت با نوارهای سایه‌زده (Shaded Ribbons):**
   - برای داده‌های پیوسته (مانند چرخه گام‌برداری)، از رسم میله‌های خطای عمودی متراکم خودداری کنید. به جای آن از نوار سایه‌زده میانگین $\pm$ یک انحراف معیار (`ax.fill_between(x, y-sd, y+sd, alpha=0.2)`) استفاده نمایید.

---

## اسکریپت‌های اجرایی در دسترس (Available Executable Scripts)

### ۱. رسم چرخه گام‌برداری (Gait Kinematics & Kinetics)
```bash
python modules/02_scientific_figures_tables/scripts/plot_gait_cycle.py --out "04_figures/knee_gait.png" --title "Knee Kinematics (n=18)"
```
خروجی: فایل تصویری PNG با وضوح ۳۰۰ دی‌پی‌آی و فایل برداری PDF برای مقالات لاتکس و ورد.

### ۲. خط لوله پردازش و رسم الکترومایوگرافی سطحی (sEMG Pipeline)
```bash
python modules/02_scientific_figures_tables/scripts/plot_emg_processing.py --out "04_figures/emg_pipeline.png"
```
خروجی: نمودار ۴ پنلی شامل سیگنال خام، فیلتر میان‌گذر (۲۰-۴۵۰ هرتز)، یک‌سوسازی و پوش خطی نرمال‌شده با MVC.

### ۳. رسم منحنی تنش-کرنش بافت‌های زیستی (Tissue Stress-Strain)
```bash
python modules/02_scientific_figures_tables/scripts/plot_stress_strain.py --out "04_figures/tendon_test.png" --tissue "Human Patellar Tendon"
```
خروجی: منحنی کامل با نمایش ناحیه انگشتی (Toe Region)، شیب مدول یانگ ($E$)، نقطه تسلیم، استحکام نهایی (UTS) و چقرمگی.

### ۴. فرمت‌بندی جداول ۳ خطی علمی (APA / IEEE Table Formatter)
```bash
python modules/02_scientific_figures_tables/scripts/table_formatter.py
```
خروجی: کدهای آماده جدول به صورت Markdown، LaTeX Booktabs، و فرمت استاندارد فارسی.
