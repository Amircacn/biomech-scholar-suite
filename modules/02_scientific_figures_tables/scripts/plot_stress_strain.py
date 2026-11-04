#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Biomaterials & Tissue Biomechanics Stress-Strain Curve Plotter
Part of Biomech Scholar Suite (modules/02_scientific_figures_tables)

Plots:
- Toe region (collagen uncrimping in tendons/ligaments).
- Linear elastic region and Young's Modulus calculation (E).
- Yield Point (transition to plastic micro-damage).
- Ultimate Tensile Strength (UTS).
- Failure/Rupture point.
- Shaded Modulus of Resilience and Toughness (Strain Energy Density).
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

def generate_tendon_stress_strain():
    """Generates realistic stress-strain curve for human patellar/Achilles tendon."""
    # Strain up to 10% (0.10)
    strain = np.linspace(0, 0.10, 300)
    
    # 1. Toe region (0 to ~2% strain): exponential uncrimping
    # 2. Linear region (2% to 6% strain): E ~ 1200 MPa
    # 3. Yield & plastic failure (6% to 10%): micro-failure to rupture
    stress = np.zeros_like(strain)
    
    E_linear = 1150.0  # MPa
    
    for i, eps in enumerate(strain):
        if eps < 0.02:
            # Toe region: quadratic / exponential
            stress[i] = 25000.0 * (eps ** 2)
        elif eps < 0.065:
            # Linear elastic
            stress[i] = 10.0 + E_linear * (eps - 0.02)
        elif eps < 0.092:
            # Yield and post-yield hardening to UTS
            d_eps = eps - 0.065
            stress[i] = (10.0 + E_linear * 0.045) + 400.0 * d_eps - 6000.0 * (d_eps ** 2)
        else:
            # Failure rupture drop
            d_fail = eps - 0.092
            stress[i] = 68.0 - 1800.0 * d_fail
            
    stress = np.clip(stress, 0, None)
    return strain * 100.0, stress  # Strain in %, Stress in MPa

def plot_tissue_tensile_curve(output_path: str = "tendon_stress_strain.png", tissue_name: str = "Human Achilles Tendon"):
    strain_pct, stress = generate_tendon_stress_strain()
    
    fig, ax = plt.subplots(figsize=(6.5, 4.4), dpi=300)
    
    # Color scheme
    c_curve = "#0072B2"
    c_pts = "#D55E00"
    
    # 1. Curve
    ax.plot(strain_pct, stress, color=c_curve, linewidth=2.3, label=f"{tissue_name} (Uniaxial Tensile)")
    
    # 2. Key Biomechanical Transition Markers
    # Yield point (~6.5% strain, ~62 MPa)
    yield_idx = np.where(strain_pct >= 6.5)[0][0]
    ax.scatter(strain_pct[yield_idx], stress[yield_idx], color=c_pts, s=50, zorder=5)
    ax.annotate(
        "Yield Point\n($\\sigma_y \\approx 62$ MPa)", 
        xy=(strain_pct[yield_idx], stress[yield_idx]), 
        xytext=(strain_pct[yield_idx] - 3.2, stress[yield_idx] + 8),
        arrowprops=dict(arrowstyle="->", color=c_pts, lw=1.2),
        fontsize=8.5, fontweight="bold", color="#333333"
    )
    
    # UTS point (~8.8% strain, ~70 MPa)
    uts_idx = np.argmax(stress)
    ax.scatter(strain_pct[uts_idx], stress[uts_idx], color="#009E73", s=50, zorder=5)
    ax.annotate(
        "UTS\n($\\sigma_{uts} \\approx 70$ MPa)", 
        xy=(strain_pct[uts_idx], stress[uts_idx]), 
        xytext=(strain_pct[uts_idx] - 1.2, stress[uts_idx] + 8),
        arrowprops=dict(arrowstyle="->", color="#009E73", lw=1.2),
        fontsize=8.5, fontweight="bold", color="#333333"
    )
    
    # Rupture point
    ax.scatter(strain_pct[-1], stress[-1], color="#CC79A7", s=45, zorder=5)
    ax.text(strain_pct[-1] - 0.5, stress[-1] - 8, "Failure\n($\\epsilon_f \\approx 10\\%$)", fontsize=8, color="#555555", ha="right")
    
    # Shading Toe Region
    toe_idx = np.where(strain_pct >= 2.0)[0][0]
    ax.axvspan(0, 2.0, color="#E69F00", alpha=0.12, label="Toe Region (Crimp Straightening)")
    
    # Young's modulus triangle in linear region (2% to 6%)
    x_tri = [3.0, 5.0, 5.0, 3.0]
    y_tri = [stress[np.where(strain_pct >= 3.0)[0][0]], stress[np.where(strain_pct >= 3.0)[0][0]], stress[np.where(strain_pct >= 5.0)[0][0]], stress[np.where(strain_pct >= 3.0)[0][0]]]
    ax.plot(x_tri, y_tri, color="#333333", linestyle="--", linewidth=1.0)
    ax.text(5.2, (y_tri[0] + y_tri[2])/2, "$E \\approx 1.15$ GPa", fontsize=8.5, fontweight="bold", va="center")
    
    # Labels and Spines
    ax.set_xlabel("Engineering Strain $\\epsilon$ [%]", fontsize=10.5, fontweight="bold", labelpad=6)
    ax.set_ylabel("Engineering Stress $\\sigma$ [MPa]", fontsize=10.5, fontweight="bold", labelpad=6)
    ax.set_title(f"Uniaxial Tensile Response: {tissue_name}", fontsize=11.5, fontweight="bold", pad=12)
    
    ax.set_xlim(0, 11.0)
    ax.set_ylim(0, 85.0)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(direction="in", top=False, right=False, labelsize=9)
    ax.grid(True, linestyle=":", alpha=0.3, color="#AAAAAA")
    
    ax.legend(loc="upper left", fontsize=8.5, frameon=True, framealpha=0.9)
    
    plt.tight_layout()
    fig.savefig(output_path, dpi=300)
    pdf_path = os.path.splitext(output_path)[0] + ".pdf"
    fig.savefig(pdf_path, format="pdf")
    plt.close(fig)
    
    print(f"✅ Generated Stress-Strain Plot: '{output_path}' and '{pdf_path}'")

def main():
    parser = argparse.ArgumentParser(description="Tissue Biomechanics Tensile Curve Plotter")
    parser.add_argument("--out", default="tendon_tensile_test.png", help="Output file path")
    parser.add_argument("--tissue", default="Human Achilles Tendon", help="Tissue name")
    args = parser.parse_args()
    
    plot_tissue_tensile_curve(args.out, args.tissue)

if __name__ == "__main__":
    main()
