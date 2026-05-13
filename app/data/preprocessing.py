import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:

    return df.drop_duplicates()


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].mean())

    return df


def preprocess_financial_data(df: pd.DataFrame):

    df = clean_column_names(df)

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    return df