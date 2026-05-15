import pandas as pd

from sklearn.linear_model import (
    LinearRegression
)

from app.forecasting.preprocessing import (
    prepare_forecasting_data
)


def forecast_future_values(
    df: pd.DataFrame,
    target_column: str,
    periods: int = 3
):

    X, y, processed_df = (
        prepare_forecasting_data(
            df,
            target_column
        )
    )

    model = LinearRegression()

    model.fit(X, y)

    future_indexes = list(
        range(
            len(processed_df),
            len(processed_df) + periods
        )
    )

    future_df = pd.DataFrame({
        "time_index": future_indexes
    })

    predictions = model.predict(
    future_df
)

    future_df["forecast"] = predictions

    future_df["forecast"] = (
        future_df["forecast"]
        .round(2)
    )
    return future_df