import pandas as pd

from sklearn.linear_model import (
    LinearRegression
)

from app.forecasting.preprocessing import (
    prepare_forecasting_data
)


# =========================================
# FORECASTING ENGINE
# =========================================

def forecast_future_values(

    df,

    target_column,

    date_column
):

    # =====================================
    # PREPARE DATA
    # =====================================

    forecast_df = (
        prepare_forecasting_data(

            df,

            target_column,

            date_column
        )
    )

    # =====================================
    # VALIDATION
    # =====================================

    if forecast_df.empty:

        raise ValueError(
            "Prepared forecasting dataset is empty."
        )

    if target_column not in forecast_df.columns:

        raise ValueError(
            f"{target_column} column missing."
        )

    if date_column not in forecast_df.columns:

        raise ValueError(
            f"{date_column} column missing."
        )

    # =====================================
    # RESET INDEX
    # =====================================

    forecast_df = (
        forecast_df.reset_index(
            drop=True
        )
    )

    # =====================================
    # CREATE TIME INDEX
    # =====================================

    forecast_df["time_index"] = (
        range(len(forecast_df))
    )

    # =====================================
    # TRAIN MODEL
    # =====================================

    X = forecast_df[
        ["time_index"]
    ]

    y = forecast_df[
        target_column
    ]

    model = LinearRegression()

    model.fit(X, y)

    # =====================================
    # FUTURE PREDICTIONS
    # =====================================

    future_indices = [

        len(forecast_df),

        len(forecast_df) + 1,

        len(forecast_df) + 2
    ]

    future_df = pd.DataFrame({

        "time_index":
        future_indices
    })

    predictions = model.predict(
        future_df
    )

    # =====================================
    # FUTURE DATES
    # =====================================

    forecast_df[
        date_column
    ] = pd.to_datetime(

        forecast_df[
            date_column
        ],

        errors="coerce"
    )

    last_date = forecast_df[
        date_column
    ].max()

    future_dates = pd.date_range(

        start=last_date,

        periods=4,

        freq="D"
    )[1:]

    # =====================================
    # OUTPUT
    # =====================================

    result_df = pd.DataFrame({

        "date": future_dates,

        "forecast": predictions
    })

    return result_df