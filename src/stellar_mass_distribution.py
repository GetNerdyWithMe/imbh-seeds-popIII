"""
Stellar mass distributions relevant to Population III star formation.

This module defines parameterized stellar mass distributions commonly
invoked in Population III studies, with direct control over mass cutoffs
and high-mass behavior. The prescriptions are intended for numerical
evaluation of remnant populations under varying physical assumptions.
"""

import numpy as np


def truncated_power_law(
    sample_size: int,
    mass_min: float,
    mass_max: float,
    slope: float
) -> np.ndarray:
    """
    Draw samples from a truncated power-law stellar mass distribution.

    The distribution is defined such that:

        dN / dM ∝ M^{-slope}

    over the interval [mass_min, mass_max].

    Parameters
    ----------
    sample_size : int
        Number of stellar masses to draw.
    mass_min : float
        Lower mass cutoff in solar masses.
    mass_max : float
        Upper mass cutoff in solar masses.
    slope : float
        Power-law exponent governing the high-mass behavior.

    Returns
    -------
    np.ndarray
        Array of sampled stellar masses in solar masses.
    """
    if sample_size <= 0:
        raise ValueError("sample_size must be positive.")

    if mass_min <= 0.0:
        raise ValueError("mass_min must be positive.")

    if mass_max <= mass_min:
        raise ValueError("mass_max must exceed mass_min.")

    if slope == 1.0:
        raise ValueError("slope = 1 produces a logarithmic divergence.")

    uniform_samples = np.random.random(sample_size)
    exponent = 1.0 - slope

    return (
        uniform_samples * (mass_max**exponent - mass_min**exponent)
        + mass_min**exponent
    ) ** (1.0 / exponent)
