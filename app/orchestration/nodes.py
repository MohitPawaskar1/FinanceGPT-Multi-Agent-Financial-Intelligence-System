from app.data.loader import (
    load_financial_data
)

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

from app.forecasting.forecaster import (
    forecast_future_values
)

from app.forecasting.commentary import (
    generate_forecast_summary
)

from app.anomaly_detection.detector import (
    detect_anomalies
)

from app.anomaly_detection.commentary import (
    generate_anomaly_summary
)

from app.rag.query_engine import (
    generate_rag_response
)


def ingestion_node(state):

    file_path = state["file_path"]

    df = load_financial_data(file_path)

    df = preprocess_financial_data(df)

    df = standardize_schema(df)

    state["df"] = df

    return state


def insight_node(state):

    df = state["df"]

    insights = generate_dataset_insights(df)

    commentary = generate_financial_commentary(
        insights
    )

    state["insights"] = insights

    state["commentary"] = commentary

    return state


def forecast_node(state):

    df = state["df"]

    forecast_df = forecast_future_values(
        df,
        target_column="revenue"
    )

    summary = generate_forecast_summary(
        forecast_df
    )

    state["forecast_summary"] = summary

    return state


def anomaly_node(state):

    df = state["df"]

    anomaly_df = detect_anomalies(df)

    summary = generate_anomaly_summary(
        anomaly_df
    )

    state["anomaly_summary"] = summary

    return state


def rag_query_node(state):

    query = state["user_query"]

    response = generate_rag_response(
        query
    )

    state["rag_response"] = response

    return state