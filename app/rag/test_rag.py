from app.data.loader import load_financial_data

from app.data.preprocessing import (
    preprocess_financial_data
)

from app.data.schema_mapper import (
    standardize_schema
)

from app.insights.extractor import (
    generate_dataset_insights
)

from app.agents.commentary_agent import (
    generate_financial_commentary
)

from app.rag.ingestion import (
    ingest_financial_analysis
)

from app.rag.retriever import (
    retrieve_relevant_context
)


def run_rag_pipeline():

    file_path = "datasets/sample_financial_data.csv"

    df = load_financial_data(file_path)

    df = preprocess_financial_data(df)

    df = standardize_schema(df)

    insights = generate_dataset_insights(df)

    commentary = generate_financial_commentary(
        insights
    )

    print("\nINSIGHTS:\n")

    print(insights)

    print("\nCOMMENTARY:\n")

    print(commentary)

    ingest_financial_analysis(
        insights,
        commentary
    )

    print("\nRETRIEVAL TEST:\n")

    results = retrieve_relevant_context(
        "strong revenue growth"
    )

    for idx, result in enumerate(results):

        print(f"\nRESULT {idx + 1}:\n")

        print(result.page_content)


if __name__ == "__main__":
    run_rag_pipeline()