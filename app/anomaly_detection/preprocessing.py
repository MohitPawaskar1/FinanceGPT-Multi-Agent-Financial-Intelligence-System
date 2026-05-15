import pandas as pd


def prepare_anomaly_features(
    df: pd.DataFrame
):

    numeric_df = df.select_dtypes(
        include=["number"]
    )

    return numeric_df