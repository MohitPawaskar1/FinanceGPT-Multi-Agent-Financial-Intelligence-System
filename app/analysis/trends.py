import pandas as pd


def calculate_growth_rate(
    df: pd.DataFrame,
    column: str
):

    if column not in df.columns:
        return df

    growth_column = f"{column}_growth"

    df[growth_column] = (
        df[column]
        .pct_change()
        .mul(100)
        .round(2)
    )

    return df