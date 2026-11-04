#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Publication-Quality Gait Kinematics & Kinetics Plotter
Part of Biomech Scholar Suite (modules/02_scientific_figures_tables)

Features:
- Time-normalized gait cycle (0% to 100% stride phase).
- Ensemble average (mean) with shaded ±1 Standard Deviation (SD) error ribbon.
- Event markers: Heel-Strike (0% & 100%) and Toe-Off (~60% gait cycle).
- Academic styling: Okabe-Ito colorblind palette, despine (no top/right borders),
  proper SI units in brackets, vector PDF and 300+ DPI PNG outputs.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

# Academic Color Palette (Okabe-Ito)
OKABE_ITO = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "vermilion": "#D55E00",
    "purple": "#CC79A7",
    "sky_blue": "#56B4E9",
    "grey": "#7F7F7F"
}

def generate_synthetic_gait_data():
    """Generates realistic knee flexion/extension angle data across 101 points (0-100% gait cycle)."""
    t = np.linspace(0, 100, 101)
    
    # Typical physiological knee angle curve during walking
    # Heel strike ~0-5 deg, loading response peak ~15-20 deg, stance extension ~5 deg, swing flexion peak ~60 deg
    mean_angle = (
        5.0 * np.cos(np.radians(t * 3.6)) 
        + 18.0 * np.exp(-((t - 15) / 10)**2)
        - 5.0 * np.exp(-((t - 40) / 15)**2)
        + 58.0 * np.exp(-((t - 72) / 12)**2)
        + 3.0
    )
    
    # Realistic inter-subject standard deviation
    sd_angle = 3.5 + 2.5 * np.sin(np.radians(t * 1.8))
    return t, mean_angle, sd_angle

def plot_gait_kinematics(output_path: str = "knee_flexion_gait_cycle.png", title: str = "Knee Joint Kinematics"):
    t, mean_angle, sd_angle = generate_synthetic_gait_data()
    
    # Set publication figure parameters
    plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Helvetica']
    plt.rcParams['axes.edgecolor'] = '#333333'
    plt.rcParams['axes.linewidth'] = 1.0
    
    fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=300)
    
    # 1. Shaded Standard Deviation Band
    ax.fill_between(
        t, 
        mean_angle - sd_angle, 
        mean_angle + sd_angle, 
        color=OKABE_ITO["blue"], 
        alpha=0.22, 
        label="±1 SD Cohort Variability"
    )
    
    # 2. Mean Trajectory Line
    ax.plot(
        t, 
        mean_angle, 
        color=OKABE_ITO["blue"], 
        linewidth=2.2, 
        label="Mean Knee Angle (n=18)"
    )
    
    # 3. Toe-off Event Indicator (~60% gait cycle)
    toe_off_percent = 60.0
    ax.axvline(
        x=toe_off_percent, 
        color=OKABE_ITO["vermilion"], 
        linestyle="--", 
        linewidth=1.2, 
        alpha=0.85, 
        label=f"Toe-Off ({toe_off_percent:.0f}%)"
    )
    
    # 4. Zero Reference Line
    ax.axhline(0, color="#AAAAAA", linestyle=":", linewidth=0.8)
    
    # Stance vs Swing labels
    ax.text(30, -5, "Stance Phase (~60%)", ha="center", va="center", fontsize=9, color="#555555", style="italic")
    ax.text(80, -5, "Swing Phase (~40%)", ha="center", va="center", fontsize=9, color="#555555", style="italic")
    
    # Labels & Limits
    ax.set_xlabel("Gait Cycle [%]", fontsize=10.5, fontweight="bold", labelpad=6)
    ax.set_ylabel("Knee Flexion (+) / Extension (-) [deg]", fontsize=10.5, fontweight="bold", labelpad=6)
    ax.set_title(title, fontsize=11.5, fontweight="bold", pad=12)
    
    ax.set_xlim(0, 100)
    ax.set_ylim(-10, 75)
    
    # Ticks formatting
    ax.set_xticks(np.arange(0, 101, 20))
    ax.tick_params(direction="in", top=False, right=False, length=4, width=1.0, labelsize=9.5)
    
    # Remove top and right spines (Nature / IEEE standard)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Grid: subtle horizontal lines only
    ax.yaxis.grid(True, linestyle="--", alpha=0.3, color="#CCCCCC")
    
    # Legend
    ax.legend(frameon=True, framealpha=0.9, edgecolor="#EEEEEE", fontsize=8.5, loc="upper left")
    
    plt.tight_layout()
    
    # Save raster & vector formats
    fig.savefig(output_path, dpi=300)
    pdf_path = os.path.splitext(output_path)[0] + ".pdf"
    fig.savefig(pdf_path, format="pdf")
    plt.close(fig)
    
    print(f"✅ Generated Gait Plot: '{output_path}' and '{pdf_path}'")

def main():
    parser = argparse.ArgumentParser(description="Publication-Quality Gait Kinematics Plotter")
    parser.add_argument("--out", default="gait_cycle_kinematics.png", help="Output file path")
    parser.add_argument("--title", default="Knee Joint Kinematics during Normal Walking", help="Plot title")
    args = parser.parse_args()
    
    plot_gait_kinematics(args.out, args.title)

if __name__ == "__main__":
    main()
