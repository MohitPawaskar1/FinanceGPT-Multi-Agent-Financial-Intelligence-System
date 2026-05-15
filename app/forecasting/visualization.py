import matplotlib.pyplot as plt


def plot_forecast(
    historical_df,
    forecast_df,
    target_column
):

    plt.figure(figsize=(10, 5))

    plt.plot(
        historical_df[target_column],
        label="Historical Data"
    )

    plt.plot(
        range(
            len(historical_df),
            len(historical_df)
            + len(forecast_df)
        ),
        forecast_df["forecast"],
        label="Forecast"
    )

    plt.legend()

    plt.title(
        f"{target_column} Forecast"
    )

    plt.xlabel("Time")

    plt.ylabel(target_column)

    plt.show()