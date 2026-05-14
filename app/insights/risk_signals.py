import pandas as pd


def detect_financial_risks(df: pd.DataFrame):

    risks = []

    if "profit" in df.columns:

        negative_profit = (
            df["profit"] < 0
        ).any()

        if negative_profit:

            risks.append(
                "Negative profit values detected."
            )

    if "expenses" in df.columns and "revenue" in df.columns:

        expense_ratio = (
            df["expenses"].sum()
            / df["revenue"].sum()
        )

        if expense_ratio > 0.8:

            risks.append(
                "Expenses consume more than 80% of revenue."
            )

    return risks