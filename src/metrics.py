"""
Finance-style performance metrics for policy comparison.
"""

import pandas as pd


def add_cost_per_ton_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds cost-per-ton efficiency metrics to the policy DataFrame.

    Assumes:
      - Gov_Impact_$B in billions
      - Firm_Impact_$B in billions
      - Abatement_MMT in million metric tons
    """
    df = df.copy()

    # $/ton = (billions $ -> $) / (MMT -> tons)
    denom_tons = df["Abatement_MMT"] * 1e6

    df["Gov_$per_ton"] = (df["Gov_Impact_$B"] * 1e9) / denom_tons
    df["Firm_$per_ton"] = (df["Firm_Impact_$B"] * 1e9) / denom_tons

    df["Total_Impact_$B"] = df["Gov_Impact_$B"] + df["Firm_Impact_$B"]
    df["Total_$per_ton"] = (df["Total_Impact_$B"] * 1e9) / denom_tons

    # Cost-per-ton undefined when abatement is 0 (baseline)
    zero_abatement = df["Abatement_MMT"] == 0
    df.loc[zero_abatement, ["Gov_$per_ton", "Firm_$per_ton", "Total_$per_ton"]] = pd.NA

    return df


