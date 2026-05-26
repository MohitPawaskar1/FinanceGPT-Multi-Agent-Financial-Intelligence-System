import pandas as pd

import numpy as np


def calculate_kpis(
    df,
    target_column
):

    series = df[
        target_column
    ]

    average_value = round(
        series.mean(),
        2
    )

    maximum_value = round(
        series.max(),
        2
    )

    minimum_value = round(
        series.min(),
        2
    )

    volatility = round(
        series.std(),
        2
    )

    growth_rate = round(

        (
            (
                series.iloc[-1]
                - series.iloc[0]
            )

            / series.iloc[0]
        ) * 100,

        2
    )

    # =====================================
    # INTERPRETATIONS
    # =====================================

    if volatility < 5:

        volatility_label = (
            "Low"
        )

    elif volatility < 20:

        volatility_label = (
            "Moderate"
        )

    else:

        volatility_label = (
            "High"
        )

    if growth_rate > 20:

        trend_strength = (
            "Strong Growth"
        )

    elif growth_rate > 0:

        trend_strength = (
            "Moderate Growth"
        )

    else:

        trend_strength = (
            "Declining"
        )

    return {

        "average_value":
        average_value,

        "maximum_value":
        maximum_value,

        "minimum_value":
        minimum_value,

        "volatility":
        volatility,

        "growth_rate":
        growth_rate,

        "volatility_label":
        volatility_label,

        "trend_strength":
        trend_strength
    }