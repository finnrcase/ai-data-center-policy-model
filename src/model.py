"""
Core deterministic model functions for the AI Data Center Policy Model.

E = Y * C
Y: electricity (TWh)
C: carbon intensity (gCO2/kWh)
E: emissions (MMT CO2 / year)
"""

from __future__ import annotations

import pandas as pd

# ---- Unit conversions ----
TWH_TO_KWH = 1e9          # 1 TWh = 1e9 kWh
GRAMS_TO_METRIC_TON = 1e-6
METRIC_TON_TO_MMT = 1e-6


def emissions_mmt(y_twh: float, c_g_per_kwh: float) -> float:
    """
    Compute emissions in million metric tons (MMT CO2/year).

    Parameters
    ----------
    y_twh : float
        Electricity consumption in TWh.
    c_g_per_kwh : float
        Carbon intensity in gCO2/kWh.

    Returns
    -------
    float
        Emissions in MMT CO2/year.
    """
    grams = y_twh * TWH_TO_KWH * c_g_per_kwh
    metric_tons = grams * GRAMS_TO_METRIC_TON
    return metric_tons * METRIC_TON_TO_MMT


def build_policy_table(policy_inputs: list[dict], baseline_emissions: float | None = None) -> pd.DataFrame:
    """
    Build a deterministic policy comparison table.

    If baseline_emissions is provided, it will be used.
    Otherwise, baseline is inferred from a row labeled 'Baseline'.

    Required keys in each dict:
      Policy, Y_TWh, C_g_per_kWh, Gov_Impact_$B, Firm_Impact_$B
    """
    df = pd.DataFrame(policy_inputs).copy()

    df["Emissions_MMT"] = df.apply(
        lambda row: emissions_mmt(row["Y_TWh"], row["C_g_per_kWh"]),
        axis=1
    )

    # Determine baseline emissions
    if baseline_emissions is not None:
        base = float(baseline_emissions)
    else:
        base_rows = df.loc[df["Policy"] == "Baseline", "Emissions_MMT"]
        if len(base_rows) == 0:
            raise ValueError("Baseline emissions not provided and no 'Baseline' row found.")
        base = float(base_rows.values[0])

    df["Abatement_MMT"] = base - df["Emissions_MMT"]
    df["Abatement_%"] = (df["Abatement_MMT"] / base) * 100

    return df
