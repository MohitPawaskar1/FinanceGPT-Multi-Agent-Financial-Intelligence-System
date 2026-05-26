def build_dashboard_plan(

    df,

    date_columns,

    numeric_columns,

    target_column
):

    plan = {

        "show_forecasting": False,

        "show_anomalies": False,

        "show_correlations": False,

        "show_distribution": False,

        "primary_chart": "line",

        "secondary_chart": None
    }

    # =====================================
    # TIME SERIES DETECTION
    # =====================================

    if len(date_columns) > 0:

        plan[
            "show_forecasting"
        ] = True

        plan[
            "show_anomalies"
        ] = True

        plan[
            "primary_chart"
        ] = "line"

    # =====================================
    # MULTI-NUMERIC DETECTION
    # =====================================

    if len(numeric_columns) >= 3:

        plan[
            "show_correlations"
        ] = True

        plan[
            "secondary_chart"
        ] = "scatter"

    # =====================================
    # SINGLE NUMERIC
    # =====================================

    if len(numeric_columns) == 1:

        plan[
            "show_distribution"
        ] = True

        plan[
            "secondary_chart"
        ] = "histogram"

    return plan