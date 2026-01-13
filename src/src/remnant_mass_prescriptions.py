"""
Remnant mass prescriptions for Population III stars.

This part defines stellar mass governments relevant to Population III
evolution and maps each government to an expected compact-object outcome.
The prescriptions reflect commonly adopted boundaries in the literature
and are intended for numerical analyses rather than detailed stellar
evolution modeling.
"""

from typing import Tuple, Optional


def remnant_outcome(
    stellar_mass: float
) -> Tuple[str, Optional[float]]:
    """
    Determine the compact remnant outcome for a Population III star.

    Parameters
    ----------
    stellar_mass : float
        Zero-age main-sequence stellar mass in solar masses.

    Returns
    -------
    outcome : str
        One of:
            - "no_remnant"
            - "black_hole"
    remnant_mass : float or None
        Remnant mass in solar masses if applicable.
        Returns None when no compact remnant is produced.
    """
    if stellar_mass <= 0.0:
        raise ValueError("stellar_mass must be positive.")

    # Core-collapse supernovae with neutron star or fallback black hole
    if 10.0 <= stellar_mass < 40.0:
        return "black_hole", 0.3 * stellar_mass

    # Direct collapse to black hole
    if 40.0 <= stellar_mass < 140.0:
        return "black_hole", 0.5 * stellar_mass

    # Pair-instability supernovae (complete disruption)
    if 140.0 <= stellar_mass <= 260.0:
        return "no_remnant", None

    # Photodisintegration-driven collapse at extreme masses
    if stellar_mass > 260.0:
        return "black_hole", 0.9 * stellar_mass

    return "no_remnant", None
