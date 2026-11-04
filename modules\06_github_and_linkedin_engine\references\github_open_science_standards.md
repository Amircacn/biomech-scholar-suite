# Open Science & GitHub Repository Standards in Biomechanics
# استانداردهای علم باز و انتشار ریپازیتوری‌های بیومکانیک در گیت‌هاب

پژوهش‌های بیومکانیک مهندسی به دلیل ماهیت چندرشته‌ای (داده‌های حرکتی، مدل‌های اسکلتی-عضلانی، پردازش سیگنال و کدها) نیازمند ساختاری بسیار شفاف در گیت‌هاب هستند تا استنادپذیری و بازتولیدپذیری (Reproducibility) آن‌ها تضمین شود.

---

## ۱. ساختار استاندارد مخزن گیت‌هاب (Repository Anatomy)

```
my-biomech-project/
├── .github/
│   └── workflows/
│       └── test_pipeline.yml     # اجرای خودکار تست‌ها در گیت‌هاب اکشنز
├── data/
│   ├── raw/                      # نمونه داده‌های C3D یا CSV سبک برای تست
│   └── processed/                # داده‌های زمانی نرمال‌شده
├── src/                          # سورس‌کد پایتون یا متلب
│   ├── __init__.py
│   ├── filters.py                # پیاده‌سازی فیلتر باترورث بدون تاخیر
│   ├── inverse_dynamics.py       # حل معادلات نیوتن-اویلر
│   └── visualization.py          # توابع رسم نمودار بر اساس استانداردهای نیچر
├── notebooks/                    # ژوپیتر نوت‌بوک‌های آموزشی گام‌به‌گام
│   └── 01_gait_analysis_demo.ipynb
├── tests/                        # تست‌های خودکار یکپارچگی کدها
│   └── test_filters.py
├── CITATION.cff                  # مشخصات استناد رسمی به پروژه
├── LICENSE                       # مجوز نرم‌افزار آزاد (MIT / Apache-2.0)
├── pyproject.toml                # وابستگی‌ها و متادیتا
├── requirements.txt              # لیست پکیج‌های پایتون با نسخه
└── README.md                     # صفحه اصلی مستندات ریپازیتوری
```

---

## ۲. ایجاد فایل استناد استاندارد (`CITATION.cff`)

فایل `CITATION.cff` در ریشه ریپازیتوری باعث می‌شود گیت‌هاب به صورت خودکار دکمه «Cite this repository» را فعال کند و خروجی‌های BibTeX و APA تولید نماید:

```yaml
cff-version: 1.2.0
message: "If you use this software or biomechanical pipeline in your research, please cite it as below."
authors:
  - family-names: "Khalouzadeh"
    given-names: "Amirhassan"
    orcid: "https://orcid.org/0000-0000-0000-0000"
    affiliation: "Department of Biomechanical Engineering"
title: "Biomech-Gait-Toolkit: Open-Source 3D Kinematics and Inverse Dynamics Pipeline"
version: 1.0.0
doi: 10.5281/zenodo.1234567
date-released: 2026-11-04
url: "https://github.com/amirhacn/biomech-gait-toolkit"
keywords:
  - biomechanics
  - gait-analysis
  - inverse-dynamics
  - motion-capture
  - opensim
```

---

## ۳. نشان‌های پویا برای بالای `README.md` (Shields.io Badges)

نشان‌ها در بالای README حس حرفه‌ای و به‌روز بودن به مخاطبان و داوران می‌دهند:

```markdown
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
```

---

## ۴. انتشار داده‌های حجیم (Large Datasets & Zenodo)
فایل‌های حجیم ضبط حرکت (مانند ده‌ها گیگابایت فایل C3D آزمودنی‌ها) نباید روی گیت‌هاب کامیت شوند.
- داده‌ها را در مخازن داده باز مانند **Zenodo** یا **Figshare** بارگذاری کنید تا شناسه دیجیتال معتبر (DOI) دریافت نمایند.
- در README لینک دانلود خودکار یا اسکریپت `download_sample_data.py` قرار دهید.
