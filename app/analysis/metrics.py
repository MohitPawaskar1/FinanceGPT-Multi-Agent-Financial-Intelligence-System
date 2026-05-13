import pandas as pd
from app.utils.formatters import format_numeric_value

def calculate_sum(df: pd.DataFrame, column: str):

    if column not in df.columns:
        return None

    return df[column].sum()


def calculate_mean(df: pd.DataFrame, column: str):

    if column not in df.columns:
        return None

    return df[column].mean()


def calculate_profit_margin(df: pd.DataFrame):

    if "revenue" not in df.columns:
        return None

    if "profit" not in df.columns:
        return None

    revenue = df["revenue"].sum()
    profit = df["profit"].sum()

    if revenue == 0:
        return 0

    return (profit / revenue) * 100

def generate_basic_kpis(df: pd.DataFrame):

    metrics = {}

    if "revenue" in df.columns:
        metrics["total_revenue"] = format_numeric_value(
            calculate_sum(df, "revenue")
        )

    if "expenses" in df.columns:
        metrics["total_expenses"] = format_numeric_value(
            calculate_sum(df, "expenses")
        )

    if "profit" in df.columns:
        metrics["total_profit"] = format_numeric_value(
            calculate_sum(df, "profit")
        )

    profit_margin = calculate_profit_margin(df)

    if profit_margin is not None:
        metrics["profit_margin"] = format_numeric_value(
            profit_margin
        )

    return metrics