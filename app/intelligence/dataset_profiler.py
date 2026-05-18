import pandas as pd


def profile_dataset(
    df: pd.DataFrame
):

    profile = {}

    profile["columns"] = (
        df.columns.tolist()
    )

    profile["dtypes"] = {
        col: str(dtype)
        for col, dtype in df.dtypes.items()
    }

    profile["numeric_columns"] = (
        df.select_dtypes(
            include=["number"]
        ).columns.tolist()
    )

    profile["categorical_columns"] = (
        df.select_dtypes(
            exclude=["number"]
        ).columns.tolist()
    )

    profile["missing_values"] = {
        col: int(df[col].isnull().sum())
        for col in df.columns
    }

    return profile