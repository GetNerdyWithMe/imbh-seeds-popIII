"""
Black hole seed evolution from Population III remnants.

This module connects stellar mass prescriptions, remnant outcomes,
cosmological time constraints, and accretion-limited growth to evaluate
the mass evolution of black hole seeds originating from Population III
stars.
"""

from typing import List

import numpy as np

from stellar_mass_distribution import truncated_power_law
from remnant_mass_prescriptions import remnant_outcome
from cosmological_time import Cosmology
from accretion_growth import grow_black_hole


def evolve_population(
    n_stars: int,
    mass_min: float,
    mass_max: float,
    slope: float,
    z_initial: float,
    z_final: float,
    radiative_efficiency: float = 0.1,
    duty_cycle: float = 1.0,
    super_eddington_factor: float = 1.0
) -> List[float]:
    """
    Evolve a population of Population III remnants to a final redshift.

    Parameters
    ----------
    n_stars : int
        Number of Population III stars.
    mass_min : float
        Minimum stellar mass.
    mass_max : float
        Maximum stellar mass.
    slope : float
        Power-law slope of the stellar mass distribution.
    z_initial : float
        Formation redshift of Population III stars.
    z_final : float
        Final redshift to which remnants are evolved.
    radiative_efficiency : float, optional
        Radiative efficiency ε.
    duty_cycle : float, optional
        Accretion duty cycle.
    super_eddington_factor : float, optional
        Factor scaling the Eddington rate.

    Returns
    -------
    List[float]
        Final black hole masses at z_final.
    """
    if z_final >= z_initial:
        raise ValueError("z_final must be less than z_initial.")

    cosmology = Cosmology()

    t_initial = cosmology.cosmic_time(z_initial)
    t_final = cosmology.cosmic_time(z_final)

    available_time = t_final - t_initial

    if available_time <= 0.0:
        raise ValueError("No cosmic time available for growth.")

    stellar_masses = truncated_power_law(
        sample_size=n_stars,
        mass_min=mass_min,
        mass_max=mass_max,
        slope=slope
    )

    final_masses: List[float] = []

    for m_star in stellar_masses:
        outcome, remnant_mass = remnant_outcome(m_star)

        if outcome != "black_hole" or remnant_mass is None:
            continue

        final_mass = grow_black_hole(
            initial_mass=remnant_mass,
            delta_time=available_time,
            radiative_efficiency=radiative_efficiency,
            duty_cycle=duty_cycle,
            super_eddington_factor=super_eddington_factor
        )

        final_masses.append(final_mass)

    return final_masses
