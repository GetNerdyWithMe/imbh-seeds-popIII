"""
Visualization utilities for Population III black hole seed calculations.

This module provides plotting functions for inspecting remnant mass
distributions and black hole growth outcomes under varying physical
assumptions.
"""

from typing import Sequence

import numpy as np
import matplotlib.pyplot as plt


def plot_remnant_mass_distribution(
    masses: Sequence[float],
    bins: int = 30
) -> None:
    """
    Plot the distribution of black hole remnant masses.

    Parameters
    ----------
    masses : Sequence[float]
        Black hole masses in solar masses.
    bins : int, optional
        Number of histogram bins.
    """
    if len(masses) == 0:
        raise ValueError("No masses provided for plotting.")

    plt.figure(figsize=(6, 4))
    plt.hist(masses, bins=bins, histtype="step", linewidth=1.5)
    plt.xlabel("Black hole mass [M☉]")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def plot_growth_outcomes(
    masses: Sequence[float]
) -> None:
    """
    Plot final black hole masses on a logarithmic scale.

    Parameters
    ----------
    masses : Sequence[float]
        Final black hole masses in solar masses.
    """
    if len(masses) == 0:
        raise ValueError("No masses provided for plotting.")

    plt.figure(figsize=(6, 4))
    plt.plot(
        np.arange(len(masses)),
        np.sort(masses),
        linestyle="none",
        marker="o",
        markersize=3
    )
    plt.yscale("log")
    plt.xlabel("Remnant index")
    plt.ylabel("Final black hole mass [M☉]")
    plt.tight_layout()
    plt.show()
