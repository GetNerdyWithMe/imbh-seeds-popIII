"""
Cosmological time relations under a flat ΛCDM cosmology.

This module provides numerical relations between redshift and cosmic
time, enforcing causal bounds relevant to early-universe mass assembly
calculations.
"""

import numpy as np
from scipy.integrate import quad


class Cosmology:
    """
    Flat ΛCDM cosmology with fixed parameters.
    """

    def __init__(
        self,
        H0: float = 67.4,
        omega_m: float = 0.315,
        omega_lambda: float = 0.685
    ):
        """
        Parameters
        ----------
        H0 : float
            Hubble constant in km s⁻¹ Mpc⁻¹.
        omega_m : float
            Matter density parameter.
        omega_lambda : float
            Dark energy density parameter.
        """
        if not np.isclose(omega_m + omega_lambda, 1.0):
            raise ValueError("Cosmology must be spatially flat.")

        self.H0 = H0
        self.omega_m = omega_m
        self.omega_lambda = omega_lambda

        # Convert H0 to inverse gigayears
        self.H0_Gyr = H0 / 977.8

    def expansion_rate(self, z: float) -> float:
        """
        Dimensionless expansion rate E(z).
        """
        return np.sqrt(
            self.omega_m * (1.0 + z)**3 + self.omega_lambda
        )

    def cosmic_time(self, z: float) -> float:
        """
        Cosmic age of the universe at redshift z.

        Returns
        -------
        float
            Cosmic time in gigayears.
        """
        if z < 0.0:
            raise ValueError("Redshift must be non-negative.")

        integrand = lambda zp: 1.0 / (
            (1.0 + zp) * self.expansion_rate(zp)
        )

        integral, _ = quad(integrand, z, np.inf)

        return integral / self.H0_Gyr
