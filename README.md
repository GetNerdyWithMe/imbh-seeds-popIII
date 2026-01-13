# imbh-seeds-popIII

**Population III Star Remnants and Intermediate-Mass Black Hole Seeds**

Quasars observed at redshifts z ≳ 7 host black holes with inferred masses approaching 10⁹ M☉ at cosmic ages below one gigayear. Any viable formation pathway must therefore satisfy strict constraints on initial seed mass, mass-growth rates, and available cosmic time.

This repository contains numerical treatments of Population III stellar remnants and their subsequent mass evolution under accretion- and merger-driven growth. The calculations examine whether physically reasonable remnant masses, coupled to standard growth prescriptions, can produce intermediate-mass black hole seeds capable of reaching quasar-scale masses within the allowed cosmological window.

Only leading-order mass assembly processes are treated. Gas effects, radiative feedback, and environmental form are not resolved. The purpose of the calculations is to present which regions of parameter space remain compatible with observed early quasar populations given conservative physical assumptions.

---

## Usage

This repository is organized as a modular numerical study. Core components are intended for direct import into analysis workflows.

Core functionality resides in `src/` and may be imported directly into
custom analysis scripts or interactive environments. A representative
end-to-end calculation is provided in:


The notebook executes a single controlled experiment:
- draws a Population III stellar population
- applies remnant mass prescriptions
- enforces cosmological time constraints
- evolves surviving black hole seeds to a target redshift
- visualizes the resulting mass distributions

No external configuration is required beyond standard scientific Python
dependencies.

---

## Assumptions

The calculations adopt the following simplifying assumptions:

- Population III stellar masses follow a parameterized truncated power law
- Remnant outcomes are assigned using mass-based prescriptions
- Cosmology is fixed to a flat ΛCDM background
- Black hole growth proceeds via accretion limited by the Eddington rate
- Accretion duty cycles and super-Eddington phases are treated explicitly

These assumptions isolate causal constraints on mass assembly without attempting detailed stellar evolution.

---

## Limitations

Several physically relevant processes are intentionally excluded:

- Radiative and mechanical feedback on accretion flows
- Environmental dependence of seed formation
- Time-dependent merger histories
- Metal enrichment and transition to Population II star formation

As a result, the calculations should be interpreted as lower-order
feasibility bounds rather than predictive models.

---

## Extensions

Natural extensions of this work include:

- Redshift-dependent duty cycles
- Explicit merger trees
- Coupling to semi-analytic galaxy formation prescriptions
- Comparison with observed high-redshift quasar mass functions

The modular structure is intended to support such extensions without
significant refactoring.
