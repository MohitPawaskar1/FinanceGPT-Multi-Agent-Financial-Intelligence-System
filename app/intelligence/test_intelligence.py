from app.data.loader import (
    load_financial_data
)

from app.data.preprocessing import (
    preprocess_financial_data
)

from app.intelligence.dataset_profiler import (
    profile_dataset
)

from app.intelligence.column_detector import (
    detect_date_columns,
    detect_numeric_targets
)

from app.intelligence.target_selector import (
    select_forecast_target
)

from app.intelligence.relevance_scorer import (
    calculate_column_scores
)


def run_intelligence_test():

    file_path = (
        "datasets/walmart_dataset.csv"
    )

    df = load_financial_data(file_path)

    df = preprocess_financial_data(df)

    profile = profile_dataset(df)

    print("\nDATASET PROFILE:\n")

    print(profile)

    date_columns = detect_date_columns(df)

    numeric_columns = detect_numeric_targets(df)

    scores = calculate_column_scores(
        df,
        numeric_columns
    )

    target_info = (
    select_forecast_target(
        df,
        numeric_columns
    )
)

    print("\nDATE COLUMNS:\n")

    print(date_columns)

    print("\nNUMERIC TARGETS:\n")

    print(numeric_columns)

    print("\nCOLUMN SCORES:\n")

    print(target_info["scores"])

    print("\nTOP TARGETS:\n")

    print(target_info["top_targets"])

    print("\nCONFIDENCE LEVEL:\n")

    print(target_info["confidence"])

    print("\nSELECTED FORECAST TARGET:\n")

    print(target_info["selected_target"])


if __name__ == "__main__":

    run_intelligence_test()