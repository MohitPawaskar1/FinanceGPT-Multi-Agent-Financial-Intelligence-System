import pandas as pd


FINANCIAL_COLUMN_MAPPINGS = {

    "revenue": [
        "revenue",
        "sales",
        "income",
        "turnover"
    ],

    "expenses": [
        "expenses",
        "cost",
        "operating_cost",
        "expenditure"
    ],

    "profit": [
        "profit",
        "net_income",
        "earnings"
    ]
}


def standardize_schema(df: pd.DataFrame):

    column_mapping = {}

    for column in df.columns:

        normalized_column = (
            column.strip()
            .lower()
            .replace(" ", "_")
        )

        matched = False

        for standard_name, possible_names in FINANCIAL_COLUMN_MAPPINGS.items():

            if normalized_column in possible_names:

                column_mapping[column] = standard_name

                matched = True

                break

        if not matched:

            column_mapping[column] = normalized_column

    df = df.rename(columns=column_mapping)

    return df