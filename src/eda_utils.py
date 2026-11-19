"""Reusable statistical helpers for the SWYNEX churn EDA."""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def wilson_ci(successes: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion (95% by default)."""
    if n <= 0:
        return (np.nan, np.nan)
    p = successes / n
    denom = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / denom
    half = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return (centre - half, centre + half)


def cramers_v(x: pd.Series, y: pd.Series) -> float:
    """Cramer's V effect size (0 = independent, 1 = perfect association)."""
    table = pd.crosstab(x, y)
    if min(table.shape) < 2:
        return 0.0
    chi2 = stats.chi2_contingency(table, correction=False)[0]
    return float(np.sqrt(chi2 / (table.values.sum() * (min(table.shape) - 1))))


def rate_table(df: pd.DataFrame, by, target: str = "churn") -> pd.DataFrame:
    """Rate of a binary target per group, with sample size and Wilson 95% CI."""
    g = df.groupby(by, observed=True)[target].agg(["sum", "count"])
    bounds = [wilson_ci(int(s), int(n)) for s, n in zip(g["sum"], g["count"])]
    return pd.DataFrame(
        {
            "n": g["count"],
            "churn_rate": g["sum"] / g["count"],
            "ci_low": [b[0] for b in bounds],
            "ci_high": [b[1] for b in bounds],
        }
    )
