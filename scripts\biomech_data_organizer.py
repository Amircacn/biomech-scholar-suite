#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Biomechanics Project & Data Organizer (سامان‌دهنده داده‌ها و پروژه‌های بیومکانیک)
Part of Biomech Scholar Suite

Creates standard 7-tier directory structure for biomechanical experiments:
- 01_raw_data/ (C3D, raw CSV, force plate, EMG, MoCap)
- 02_processed_data/ (Filtered signals, normalized gait cycles, time-series)
- 03_scripts/ (MATLAB / Python / OpenSim pipelines)
- 04_figures/ (Publication-quality vector and high-DPI raster graphs)
- 05_lab_reports/ (Formatted docx and markdown lab reports)
- 06_presentations/ (PowerPoint and slide decks)
- 07_manuscripts/ (Bilingual research papers and thesis chapters)
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
import os
import json
import argparse
from datetime import datetime

STRUCTURE = {
    "01_raw_data": {
        "mocap_c3d": "فایل‌های سه‌بعدی ضبط حرکت (C3D, TRC)",
        "force_plate": "داده‌های نیروی عکس‌العمل زمین (GRF, CoP)",
        "emg_raw": "سیگنال‌های خام الکترومایوگرافی سطحی (sEMG)",
        "materials_raw": "داده‌های خام آزمون کشش، فشار یا تریبولوژی بافت"
    },
    "02_processed_data": {
        "filtered_kinematics": "زوایای مفصلی فیلتر شده (Butterworth 6Hz)",
        "normalized_gait_cycles": "چرخه‌های گام‌برداری نرمال‌شده ۰ تا ۱۰۰ درصد",
        "emg_linear_envelopes": "پوش خطی و نرمال‌سازی با MVC",
        "kinetic_moments_powers": "گشتاور و توان مفصلی استخراج‌شده از دینامیک معکوس"
    },
    "03_scripts": {
        "python": "اسکریپت‌های پایتون (پردازش داده، برازش، یادگیری ماشین)",
        "matlab": "ام‌فایل‌های متلب (فیلترگذاری، پردازش سیگنال، استخراج فازها)",
        "opensim_models": "مدل‌های اسکلتی-عضلانی و فایل‌های تنظیمات (.osim, .xml)"
    },
    "04_figures": {
        "publication_vector": "نمودارهای برداری برای مقالات (PDF, SVG, EPS)",
        "presentation_rasters": "تصاویر با وضوح بالا برای ارائه (PNG 300DPI)",
        "diagrams_and_models": "فلوچارت‌ها و نمودارهای شماتیک آزمایش"
    },
    "05_lab_reports": {
        "drafts": "پیش‌نویس‌های اولیه و یادداشت‌های آزمایشگاهی",
        "final_submissions": "گزارش‌های نهایی تأیید شده (DOCX, PDF)"
    },
    "06_presentations": {
        "lab_meetings": "اسلایدهای جلسات هفتگی و گزارش پیشرفت به استاد",
        "conference_seminar": "ارائه‌های همایش، سمینار و دفاع پایان‌نامه"
    },
    "07_manuscripts": {
        "persian": "نسخه‌های فارسی (مقالات کنفرانس داخلی، بخش‌های پایان‌نامه)",
        "english": "نسخه‌های انگلیسی (مقالات ژورنال‌های بین‌المللی J Biomech, IEEE)"
    }
}

METADATA_TEMPLATE = {
    "project_name": "Biomechanics Research Project",
    "lead_researcher": "Student / Researcher Name",
    "institution": "Department of Biomechanical Engineering",
    "created_at": datetime.now().strftime("%Y-%m-%d"),
    "instrumentation": {
        "mocap_system": "Vicon / Qualisys (Sampling Rate: 100 Hz)",
        "force_plates": "Kistler / AMTI (Sampling Rate: 1000 Hz)",
        "emg_system": "Delsys Trigno (Sampling Rate: 2000 Hz, Bandpass 20-450 Hz)",
        "material_testing": "Instron / Zwick Tensile Machine"
    },
    "subjects_summary": {
        "total_subjects": 0,
        "population": "Healthy adults / Athletes / Clinical cohort",
        "inclusion_criteria": "No history of lower-limb musculoskeletal injuries within past 6 months"
    },
    "data_protocol": {
        "filtering_kinematics": "4th order zero-lag low-pass Butterworth at 6 Hz",
        "filtering_emg": "Bandpass 20-450 Hz, rectified, low-pass 6 Hz for linear envelope",
        "time_normalization": "101 points (0% to 100% of gait cycle / trial duration)"
    }
}

def init_workspace(target_dir: str, project_name: str = "Biomechanics_Project"):
    """Initialize clean standardized project workspace."""
    base_path = os.path.join(target_dir, project_name)
    os.makedirs(base_path, exist_ok=True)
    
    print(f"🚀 ایجاد پوشه‌بندی استاندارد بیومکانیک در: {base_path}")
    
    for top_dir, sub_dirs in STRUCTURE.items():
        top_path = os.path.join(base_path, top_dir)
        os.makedirs(top_path, exist_ok=True)
        
        # Write category readme
        readme_path = os.path.join(top_path, "README.md")
        with open(readme_path, "w", encoding="utf-8") as rf:
            rf.write(f"# {top_dir}\n\n")
            rf.write("زیرپوشه‌ها و محتوای هدف:\n\n")
            for sub, desc in sub_dirs.items():
                rf.write(f"- `{sub}/`: {desc}\n")
                sub_path = os.path.join(top_path, sub)
                os.makedirs(sub_path, exist_ok=True)
                
    # Create experiment_metadata.json
    meta = METADATA_TEMPLATE.copy()
    meta["project_name"] = project_name
    meta_path = os.path.join(base_path, "experiment_metadata.json")
    with open(meta_path, "w", encoding="utf-8") as mf:
        json.dump(meta, mf, ensure_ascii=False, indent=2)
        
    # Create root README.md
    root_readme = os.path.join(base_path, "README.md")
    with open(root_readme, "w", encoding="utf-8") as rrf:
        rrf.write(f"# {project_name}\n\n")
        rrf.write("پروژه استاندارد بیومکانیک مهندسی (Standard Biomechanical Engineering Workspace)\n\n")
        rrf.write("## ساختار پوشه‌بندی و گردش‌کار داده‌ها (7-Tier Architecture)\n\n")
        rrf.write("| شماره | پوشه | توضیحات | فرمت‌های استاندارد |\n")
        rrf.write("|---|---|---|---|\n")
        rrf.write("| ۰۱ | `01_raw_data/` | داده‌های دست‌نخورده از تجهیزات آزمایشگاهی | `.c3d`, `.trc`, `.csv`, `.dat` |\n")
        rrf.write("| ۰۲ | `02_processed_data/` | داده‌های فیلتر شده و نرمال‌شده زمانی | `.mat`, `.csv`, `.parquet` |\n")
        rrf.write("| ۰۳ | `03_scripts/` | اسکریپت‌های پایتون، متلب و اپن‌سیم | `.py`, `.m`, `.osim` |\n")
        rrf.write("| ۰۴ | `04_figures/` | نمودارهای برداری آماده چاپ و ارائه | `.pdf`, `.svg`, `.png` |\n")
        rrf.write("| ۰۵ | `05_lab_reports/` | گزارش‌های آزمایشگاه دانشگاهی و سازمانی | `.docx`, `.pdf`, `.md` |\n")
        rrf.write("| ۰۶ | `06_presentations/` | ارائه‌های جلسات، همایش و دفاع پایان‌نامه | `.pptx`, `.pdf` |\n")
        rrf.write("| ۰۷ | `07_manuscripts/` | مقالات دوزبانه و فصول پایان‌نامه | `.tex`, `.docx`, `.md` |\n\n")
        rrf.write("## اعتبارسنجی و تکرارپذیری\n")
        rrf.write("مشخصات آزمایشگاهی و تنظیمات فیلترها در فایل `experiment_metadata.json` ذخیره شده است.\n")

    print("✅ ایجاد پوشه‌بندی استاندارد با موفقیت پایان یافت!")
    print(f"📁 فایل متادیتا در: {meta_path}")

def main():
    parser = argparse.ArgumentParser(description="Biomechanics Standard Workspace Initializer")
    parser.add_argument("--dir", default=".", help="Target root directory")
    parser.add_argument("--name", default="Biomech_Project", help="Project folder name")
    args = parser.parse_args()
    
    init_workspace(args.dir, args.name)

if __name__ == "__main__":
    main()
