"""
Accretion-limited black hole mass growth.

This module defines mass growth under Eddington-limited accretion with
explicit control over radiative efficiency, duty cycle, and optional
super-Eddington phases. Growth is evaluated as a function of available
cosmic time rather than arbitrary iteration steps.
"""

import numpy as np


def eddington_timescale(
    radiative_efficiency: float
) -> float:
    """
    Eddington e-folding timescale.

    Parameters
    ----------
    radiative_efficiency : float
        Radiative efficiency ε.

    Returns
    -------
    float
        Eddington timescale in gigayears.
    """
    if not (0.0 < radiative_efficiency < 1.0):
        raise ValueError("Radiative efficiency must lie between 0 and 1.")

    return 0.45 * radiative_efficiency / (1.0 - radiative_efficiency)


def grow_black_hole(
    initial_mass: float,
    delta_time: float,
    radiative_efficiency: float = 0.1,
    duty_cycle: float = 1.0,
    super_eddington_factor: float = 1.0
) -> float:
    """
    Compute black hole mass growth over a fixed cosmic time interval.

    Parameters
    ----------
    initial_mass : float
        Initial black hole mass in solar masses.
    delta_time : float
        Available cosmic time in gigayears.
    radiative_efficiency : float, optional
        Radiative efficiency ε.
    duty_cycle : float, optional
        Fraction of time spent accreting (0 ≤ f ≤ 1).
    super_eddington_factor : float, optional
        Multiplicative factor applied to the Eddington rate.

    Returns
    -------
    float
        Final black hole mass in solar masses.
    """
    if initial_mass <= 0.0:
        raise ValueError("Initial mass must be positive.")

    if delta_time < 0.0:
        raise ValueError("delta_time must be non-negative.")

    if not (0.0 <= duty_cycle <= 1.0):
        raise ValueError("Duty cycle must lie between 0 and 1.")

    if super_eddington_factor <= 0.0:
        raise ValueError("super_eddington_factor must be positive.")

    t_edd = eddington_timescale(radiative_efficiency)

    effective_time = delta_time * duty_cycle * super_eddington_factor

    return initial_mass * np.exp(effective_time / t_edd)
