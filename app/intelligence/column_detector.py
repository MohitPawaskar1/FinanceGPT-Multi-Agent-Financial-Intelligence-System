import pandas as pd


# =========================================
# DATE COLUMN DETECTION
# =========================================

def detect_date_columns(df):

    detected_dates = []

    for column in df.columns:

        column_lower = (
            column.lower()
        )

        # =================================
        # NAME-BASED DETECTION
        # =================================

        if any(

            keyword in column_lower

            for keyword in [

                "date",

                "time",

                "timestamp",

                "created",

                "booking",

                "invoice"
            ]
        ):

            detected_dates.append(
                column
            )

            continue

        # =================================
        # DATETIME PARSE TEST
        # =================================

        try:

            parsed = pd.to_datetime(
                df[column]
            )

            if (
                parsed.notna().sum()
                > len(df) * 0.7
            ):

                detected_dates.append(
                    column
                )

        except:

            pass

    return list(
        set(detected_dates)
    )


# =========================================
# NUMERIC TARGET DETECTION
# =========================================

def detect_numeric_targets(df):

    numeric_columns = []

    for column in df.columns:

        if pd.api.types.is_numeric_dtype(
            df[column]
        ):

            # Exclude binary columns

            unique_values = (
                df[column].nunique()
            )

            if unique_values > 5:

                numeric_columns.append(
                    column
                )

    return numeric_columns