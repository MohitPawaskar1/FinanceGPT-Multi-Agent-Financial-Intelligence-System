import pandas as pd


def prepare_forecasting_data(
    df: pd.DataFrame,
    target_column: str
):

    forecast_df = df.copy()

    forecast_df["date"] = pd.to_datetime(
        forecast_df["date"]
    )

    forecast_df = forecast_df.sort_values(
        by="date"
    )

    forecast_df["time_index"] = range(
        len(forecast_df)
    )

    X = forecast_df[["time_index"]]

    y = forecast_df[target_column]

    return X, y, forecast_df