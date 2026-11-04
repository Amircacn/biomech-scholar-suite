#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Surface EMG (sEMG) Signal Processing & Multi-Panel Visualization
Part of Biomech Scholar Suite (modules/02_scientific_figures_tables)

Workflow:
1. Raw EMG Acquisition (2000 Hz).
2. 4th-order zero-lag Bandpass Filter (20-450 Hz Butterworth).
3. Full-Wave Rectification (|x|).
4. Linear Envelope via Low-Pass Filter (6 Hz Butterworth).
5. Normalization against Maximum Voluntary Contraction (% MVC).
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import os
import argparse

def generate_synthetic_emg(duration: float = 3.0, fs: int = 2000):
    """Generates synthetic EMG burst during muscle activation."""
    t = np.linspace(0, duration, int(duration * fs))
    # Gaussian noise baseline
    raw_noise = np.random.normal(0, 0.04, len(t))
    
    # Activation burst between 1.0s and 2.0s
    envelope_true = np.exp(-((t - 1.5) / 0.25)**2)
    burst = envelope_true * np.random.normal(0, 0.45, len(t))
    
    # Combined raw signal with motion artifact (low freq hum) and 50Hz electrical noise
    artifact = 0.08 * np.sin(2 * np.pi * 5 * t) + 0.03 * np.sin(2 * np.pi * 50 * t)
    raw_signal = burst + raw_noise + artifact
    return t, raw_signal, fs

def process_emg(raw_signal, fs: int = 2000, mvc_peak_voltage: float = 0.55):
    """Processes raw EMG into bandpass, rectified, and normalized linear envelope."""
    # 1. Bandpass filter 20-450 Hz (Butterworth 4th order zero-lag)
    nyq = 0.5 * fs
    low = 20.0 / nyq
    high = 450.0 / nyq
    b_band, a_band = butter(4, [low, high], btype='band')
    filtered_signal = filtfilt(b_band, a_band, raw_signal)
    
    # 2. Full-wave Rectification
    rectified_signal = np.abs(filtered_signal)
    
    # 3. Linear Envelope (Low-pass 6 Hz Butterworth 4th order zero-lag)
    low_cutoff = 6.0 / nyq
    b_low, a_low = butter(4, low_cutoff, btype='low')
    envelope = filtfilt(b_low, a_low, rectified_signal)
    
    # 4. MVC Normalization (% MVC)
    norm_envelope = (envelope / mvc_peak_voltage) * 100.0
    return filtered_signal, rectified_signal, norm_envelope

def plot_emg_pipeline(output_path: str = "emg_processing_pipeline.png"):
    t, raw, fs = generate_synthetic_emg()
    filtered, rectified, norm_env = process_emg(raw, fs)
    
    fig, axes = plt.subplots(4, 1, figsize=(7.2, 7.5), sharex=True, dpi=300)
    
    # Color definition
    c_raw = "#4A4A4A"
    c_filt = "#0072B2"
    c_rect = "#E69F00"
    c_env = "#D55E00"
    
    # 1. Raw EMG
    axes[0].plot(t, raw, color=c_raw, linewidth=0.7)
    axes[0].set_ylabel("Raw EMG\n[mV]", fontsize=9, fontweight="bold")
    axes[0].set_title("Surface EMG Signal Conditioning Pipeline (Tibialis Anterior)", fontsize=11, fontweight="bold", pad=8)
    
    # 2. Bandpassed EMG
    axes[1].plot(t, filtered, color=c_filt, linewidth=0.7)
    axes[1].set_ylabel("Bandpassed\n(20-450 Hz) [mV]", fontsize=9, fontweight="bold")
    
    # 3. Rectified EMG
    axes[2].plot(t, rectified, color=c_rect, linewidth=0.7)
    axes[2].set_ylabel("Full-Wave\nRectified [mV]", fontsize=9, fontweight="bold")
    
    # 4. Linear Envelope (% MVC)
    axes[3].plot(t, norm_env, color=c_env, linewidth=2.0, label="Linear Envelope (6 Hz Cutoff)")
    axes[3].set_ylabel("Muscle Act.\n[% MVC]", fontsize=9, fontweight="bold")
    axes[3].set_xlabel("Time [s]", fontsize=10, fontweight="bold")
    axes[3].legend(loc="upper right", fontsize=8.5, frameon=True)
    
    # Formatting each panel
    for ax in axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(direction="in", top=False, right=False, labelsize=8.5)
        ax.grid(True, linestyle=":", alpha=0.3, color="#888888")
        
    axes[3].set_xlim(0, 3.0)
    
    plt.tight_layout()
    fig.savefig(output_path, dpi=300)
    pdf_path = os.path.splitext(output_path)[0] + ".pdf"
    fig.savefig(pdf_path, format="pdf")
    plt.close(fig)
    
    print(f"✅ Generated EMG Pipeline Plot: '{output_path}' and '{pdf_path}'")

def main():
    parser = argparse.ArgumentParser(description="sEMG Processing & Publication Plotter")
    parser.add_argument("--out", default="emg_processing_pipeline.png", help="Output image file")
    args = parser.parse_args()
    
    plot_emg_pipeline(args.out)

if __name__ == "__main__":
    main()
