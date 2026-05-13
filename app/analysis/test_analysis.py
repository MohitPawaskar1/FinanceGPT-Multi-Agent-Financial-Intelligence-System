from app.data.loader import load_financial_data
from app.data.preprocessing import preprocess_financial_data

from app.data.schema_mapper import standardize_schema

from app.data.metadata_extractor import extract_metadata

from app.analysis.metrics import generate_basic_kpis
from app.analysis.trends import calculate_growth_rate
from app.analysis.summary import generate_financial_summary
from app.data.semantic_mapper import analyze_dataset_schema


def run_analysis_pipeline():

    file_path = "datasets/sample_financial_data.csv"

    df = load_financial_data(file_path)

    print("\nRAW DATA:\n")
    print(df)

    df = preprocess_financial_data(df)

    print("\nPREPROCESSED DATA:\n")
    print(df)

    df = standardize_schema(df)

    print("\nSTANDARDIZED SCHEMA:\n")
    print(df.columns)

    metadata = extract_metadata(df)

    print("\nDATASET METADATA:\n")
    print(metadata)

    semantic_analysis = analyze_dataset_schema(df)

    print("\nSEMANTIC ANALYSIS:\n")

    print(semantic_analysis)

    kpis = generate_basic_kpis(df)

    print("\nBASIC KPIs:\n")
    print(kpis)

    if "revenue" in df.columns:

        df = calculate_growth_rate(
            df,
            "revenue"
        )

        print("\nREVENUE GROWTH:\n")

        print(
            df[
                ["revenue", "revenue_growth"]
            ]
        )

    print("\nEXECUTIVE SUMMARY:\n")

    print(generate_financial_summary(df))


if __name__ == "__main__":
    run_analysis_pipeline()