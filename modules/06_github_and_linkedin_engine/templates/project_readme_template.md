<div align="center">

# 🦾 OpenBiomech-Gait: 3D Kinematics & Inverse Dynamics Toolkit
### ابزار متن‌باز تحلیل سه‌بعدی حرکت، پردازش C3D و دینامیک معکوس اندام تحتانی

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-0072B2.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-E69F00.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-009E73.svg)](https://github.com/your-username/openbiomech-gait)

</div>

---

## 📖 Overview | معرفی پروژه

**OpenBiomech-Gait** is an open-source Python pipeline designed for biomechanical researchers and clinical gait analysts. It parses 3D motion capture files (`.c3d`, `.trc`), synchronizes ground reaction force (GRF) plate data, executes digital zero-lag Butterworth filtering, and calculates sagittal-plane joint kinematics and inverse dynamics moments conforming to the **International Society of Biomechanics (ISB)** recommendations.

این پکیج یک خط لوله کامل پایتون برای پردازش فایل‌های سه‌بعدی ضبط حرکت، فیلترگذاری باترورث بدون شیفت فاز، محاسبه زوایای مفصلی کاردان/اویلر، استخراج گشتاور و توان مفصلی از طریق دینامیک معکوس و ترسیم نمودارهای آماده چاپ مقالات علمی است.

---

## ✨ Key Features | قابلیت‌های کلیدی

- **C3D & TRC Parser:** High-speed parsing of 3D optical trajectories and analog force plate channels.
- **Signal Conditioning:** 4th-order zero-phase Butterworth filtering with automatic residual analysis cutoff selection (Winter method).
- **Time Normalization:** Gait cycle event detection (Heel-Strike to Toe-Off) normalized across 101 points ($0\%$ to $100\%$).
- **Recursive Inverse Dynamics:** Bottom-up 3D Newton-Euler equations yielding net internal moments and mechanical joint power.
- **Publication Graphics:** Automatic generation of publication-quality vector plots (PDF/SVG) with $\pm 1$ SD shaded bands adhering to Nature and IEEE styling.
- **Bilingual Documentation:** Full documentation and API references in both English and Persian.

---

## 📂 Repository Structure | ساختار مخزن

```text
├── data/
│   ├── raw/                      # Sample .c3d and force plate files
│   └── processed/                # Normalized 101-point gait cycles
├── src/
│   ├── __init__.py
│   ├── c3d_parser.py             # BTK / ezc3d interface
│   ├── filters.py                # 4th-order Butterworth implementation
│   ├── kinematics.py             # ISB Euler/Cardan joint angles
│   ├── inverse_dynamics.py       # Newton-Euler equations of motion
│   └── plotting.py               # Publication figure generator
├── examples/
│   └── process_sample_trial.py   # Complete end-to-end tutorial
├── tests/
│   └── test_inverse_dynamics.py  # Unit tests against benchmark datasets
├── CITATION.cff                  # Citation metadata
├── requirements.txt              # Production dependencies
└── README.md
```

---

## ⚡ Quick Start | شروع سریع

### 1. Installation | نصب
```bash
git clone https://github.com/your-username/openbiomech-gait.git
cd openbiomech-gait
pip install -r requirements.txt
```

### 2. Run Example Pipeline | اجرای نمونه
```python
from src.c3d_parser import load_trial
from src.inverse_dynamics import compute_joint_kinetics
from src.plotting import plot_gait_cycle

# Load raw trial data
trial = load_trial("data/raw/sample_gait_01.c3d")

# Process kinematics and net knee moments
results = compute_joint_kinetics(trial, cutoff_freq=6.0)

# Export publication plot
plot_gait_cycle(results, output_path="knee_kinetics_publication.pdf")
```

---

## 📊 Sample Output | نمونه خروجی

| Parameter | Control Cohort ($n=12$) | Assistive Condition ($n=12$) | $p$-value |
|---|:---:|:---:|:---:|
| Peak Knee Flexion [$^\circ$] | $62.4 \pm 4.1$ | $61.8 \pm 3.9$ | $0.420$ |
| Peak Knee Extension Moment [$N\cdot m/kg$] | $1.34 \pm 0.18$ | $1.08 \pm 0.14$ | $0.002^*$ |
| Vertical Impact Peak [$BW$] | $1.18 \pm 0.09$ | $1.15 \pm 0.07$ | $0.184$ |

---

## 📜 Citation | نحوه ارجاع علمی

If you use this toolkit in your academic publications, please cite:

```bibtex
@software{khalouzadeh2026openbiomech,
  author       = {Khalouzadeh, Amirhassan},
  title        = {OpenBiomech-Gait: 3D Kinematics & Inverse Dynamics Toolkit},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.1234567},
  url          = {https://github.com/your-username/openbiomech-gait}
}
```

---

## 🤝 Contributing & License | مشارکت و مجوز

Contributions are welcome! Please check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.  
Distributed under the **MIT License**. See `LICENSE` for details.
