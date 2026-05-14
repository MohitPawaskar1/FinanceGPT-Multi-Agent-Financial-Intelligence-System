from app.data.loader import load_financial_data

from app.data.preprocessing import (
    preprocess_financial_data
)

from app.data.schema_mapper import (
    standardize_schema
)

from app.data.metadata_extractor import (
    extract_metadata
)

from app.data.semantic_mapper import (
    analyze_dataset_schema
)

from app.analysis.metrics import (
    generate_basic_kpis
)

from app.analysis.summary import (
    generate_financial_summary
)

from app.agents.commentary_agent import (
    generate_financial_commentary
)

from app.insights.extractor import (
    generate_dataset_insights
)

def run_commentary_pipeline():

    file_path = "datasets/sample_financial_data.csv"

    df = load_financial_data(file_path)

    df = preprocess_financial_data(df)

    df = standardize_schema(df)

    metadata = extract_metadata(df)

    semantic_analysis = analyze_dataset_schema(df)

    kpis = generate_basic_kpis(df)

    summary = generate_financial_summary(df)

    insights = generate_dataset_insights(df)

    print("\nGENERATED INSIGHTS:\n")

    print(insights)

    commentary = generate_financial_commentary(
        insights
    )

    print("\nAI FINANCIAL COMMENTARY:\n")

    print(commentary)


if __name__ == "__main__":
    run_commentary_pipeline()