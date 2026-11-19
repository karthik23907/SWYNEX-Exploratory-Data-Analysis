import numpy as np
import pandas as pd
import pytest

from src.eda_utils import cramers_v, rate_table, wilson_ci


def test_wilson_ci_known_value():
    lo, hi = wilson_ci(50, 100)
    assert lo == pytest.approx(0.404, abs=0.002)
    assert hi == pytest.approx(0.596, abs=0.002)


def test_wilson_ci_edges_stay_in_unit_interval():
    lo0, hi0 = wilson_ci(0, 20)
    lo1, hi1 = wilson_ci(20, 20)
    assert lo0 == pytest.approx(0.0, abs=1e-9) and 0 < hi0 < 1
    assert 0 < lo1 < 1 and hi1 == pytest.approx(1.0, abs=1e-9)


def test_wilson_ci_empty_group_is_nan():
    assert all(np.isnan(wilson_ci(0, 0)))


def test_cramers_v_perfect_and_independent():
    y = pd.Series([0, 0, 1, 1] * 25)
    assert cramers_v(y, y) == pytest.approx(1.0)
    x = pd.Series(["a", "b"] * 50)
    assert cramers_v(x, y) == pytest.approx(0.0, abs=1e-9)


def test_cramers_v_constant_column_is_zero():
    assert cramers_v(pd.Series(["a"] * 10), pd.Series([0, 1] * 5)) == 0.0


def test_rate_table_counts_and_rates():
    df = pd.DataFrame({"g": ["x"] * 10 + ["y"] * 20, "churn": [1] * 5 + [0] * 5 + [1] * 4 + [0] * 16})
    t = rate_table(df, "g")
    assert t.loc["x", "n"] == 10 and t.loc["x", "churn_rate"] == pytest.approx(0.5)
    assert t.loc["y", "churn_rate"] == pytest.approx(0.2)
    assert (t.ci_low <= t.churn_rate).all() and (t.churn_rate <= t.ci_high).all()
