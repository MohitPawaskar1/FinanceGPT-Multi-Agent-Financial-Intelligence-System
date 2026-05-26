import pandas as pd


# =========================================
# FORECAST PREPROCESSING
# =========================================

def prepare_forecasting_data(

    df,

    target_column,

    date_column
):

    forecast_df = df[[
        date_column,
        target_column
    ]].copy()

    # =====================================
    # DATE CONVERSION
    # =====================================

    forecast_df[
        date_column
    ] = pd.to_datetime(

        forecast_df[
            date_column
        ],

        errors="coerce"
    )

    # =====================================
    # REMOVE INVALID ROWS
    # =====================================

    forecast_df = (
        forecast_df.dropna()
    )

    # =====================================
    # SORT VALUES
    # =====================================

    forecast_df = (
        forecast_df.sort_values(
            by=date_column
        )
    )

    return forecast_df