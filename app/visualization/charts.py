import plotly.express as px

import pandas as pd


# =========================================
# CLEAN THEME
# =========================================

CHART_THEME = "plotly_dark"


# =========================================
# HISTOGRAM
# =========================================

def generate_histogram(

    df,

    column
):

    fig = px.histogram(

        df,

        x=column,

        nbins=30,

        title=f"{column} Distribution",

        color_discrete_sequence=[
            "#4F8BF9"
        ],

        template=CHART_THEME
    )

    return fig


# =========================================
# PIE CHART
# =========================================

def generate_pie_chart(

    df,

    column
):

    value_counts = (
        df[column]
        .value_counts()
        .head(5)
    )

    fig = px.pie(

        names=value_counts.index,

        values=value_counts.values,

        title=f"{column} Breakdown",

        template=CHART_THEME
    )

    return fig


# =========================================
# AGGREGATED TREND CHART
# =========================================
def generate_trend_chart(

    df,

    date_column,

    target_column
):

    trend_df = df[[
        date_column,
        target_column
    ]].copy()

    # =====================================
    # CONVERT DATE
    # =====================================

    trend_df[date_column] = pd.to_datetime(

        trend_df[date_column],

        errors="coerce"
    )

    trend_df = trend_df.dropna()

    # =====================================
    # DAILY AGGREGATION
    # =====================================

    trend_df["day"] = (
        trend_df[date_column]
        .dt.date
    )

    trend_df = (
        trend_df.groupby("day")
        [target_column]
        .mean()
        .reset_index()
    )

    # =====================================
    # SORT
    # =====================================

    trend_df = (
        trend_df.sort_values(
            by="day"
        )
    )

    # =====================================
    # CHART
    # =====================================

    fig = px.line(

        trend_df,

        x="day",

        y=target_column,

        title=f"Daily {target_column} Trend",

        template=CHART_THEME
    )

    fig.update_traces(

        line=dict(

            color="#4F8BF9",

            width=4
        )
    )

    fig.update_layout(

        xaxis_title="Date",

        yaxis_title=target_column,

        title_font_size=20
    )

    return fig