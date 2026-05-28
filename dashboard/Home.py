import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

import streamlit as st
import requests
import pandas as pd

from app.data.loader import (
    load_financial_data
)

from app.data.preprocessing import (
    preprocess_financial_data
)

from app.visualization.charts import (

    generate_histogram,

    generate_pie_chart
)

from app.intelligence.kpi_engine import (
    calculate_kpis
)

from dashboard.styles import (
    apply_dashboard_styling
)


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(

    page_title="FinanceGPT",

    layout="wide"
)

apply_dashboard_styling()


# =========================================
# HEADER
# =========================================

st.title(
    "FinanceGPT Executive Workspace"
)

st.markdown(
    """
AI-Powered Financial Intelligence Platform
for Dynamic Business Analytics,
Forecasting, and Risk Detection
"""
)

st.divider()


# =========================================
# SESSION STATE
# =========================================

if "file_path" not in st.session_state:

    st.session_state["file_path"] = None


# =========================================
# SAFE API REQUEST
# =========================================

def safe_post_request(
    url,
    files=None,
    json_data=None
):

    try:

        response = requests.post(

            url,

            files=files,

            json=json_data,

            timeout=120
        )

        if response.status_code != 200:

            st.error(
                f"""
API Error

Status Code:
{response.status_code}

Response:
{response.text}
"""
            )

            return None

        try:

            return response.json()

        except Exception:

            st.error(
                f"""
Invalid JSON Response

Raw Response:

{response.text}
"""
            )

            return None

    except Exception as e:

        st.error(
            f"""
Backend Connection Error

{e}
"""
        )

        return None


# =========================================
# DATASET UPLOAD
# =========================================

uploaded_file = st.file_uploader(

    "Upload CSV or Excel Dataset",

    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    with st.spinner(
        "Uploading dataset..."
    ):

        files = {

            "uploaded_file": (

                uploaded_file.name,

                uploaded_file,

                uploaded_file.type
            )
        }

        result = safe_post_request(

            "https://financegpt-multi-agent-financial.onrender.com/upload/",

            files=files
        )

        if result is not None:

            st.session_state["file_path"] = (
                result["file_path"]
            )

            st.session_state["target_info"] = (
                result["target_info"]
            )

            st.session_state["columns"] = (
                result["columns"]
            )

            st.session_state["shape"] = (
                result["shape"]
            )

            st.session_state["preview"] = (
                result["preview"]
            )

            st.session_state["numeric_columns"] = (
                result["numeric_columns"]
            )

            st.success(
                "Dataset uploaded successfully."
            )


# =========================================
# MAIN DASHBOARD
# =========================================

if st.session_state["file_path"] is not None:

    # =====================================
    # LOAD DATA
    # =====================================

    df = load_financial_data(
        st.session_state["file_path"]
    )

    df = preprocess_financial_data(df)

    target_info = (
        st.session_state[
            "target_info"
        ]
    )

    target_column = (
        target_info[
            "selected_target"
        ]
    )

    # =====================================
    # KPI ENGINE
    # =====================================

    kpis = calculate_kpis(

        df,

        target_column
    )

    # =====================================
    # EXECUTIVE KPI OVERVIEW
    # =====================================

    st.subheader(
        "Executive KPI Overview"
    )

    kpi1, kpi2, kpi3, kpi4 = (
        st.columns(4)
    )

    with kpi1:

        st.metric(

            "Average Value",

            kpis[
                "average_value"
            ]
        )

    with kpi2:

        st.metric(

            "Maximum Value",

            kpis[
                "maximum_value"
            ]
        )

    with kpi3:

        st.metric(

            "Minimum Value",

            kpis[
                "minimum_value"
            ]
        )

    with kpi4:

        st.metric(

            "Business Trend",

            kpis[
                "trend_strength"
            ]
        )

    st.divider()

    # =====================================
    # EXECUTIVE VISUAL ANALYTICS
    # =====================================

    st.subheader(
        "Executive Visual Analytics"
    )

    chart_col1, chart_col2 = (
        st.columns(2)
    )

    # =====================================
    # HISTOGRAM
    # =====================================

    with chart_col1:

        try:

            histogram_chart = (
                generate_histogram(

                    df,

                    target_column
                )
            )

            st.plotly_chart(

                histogram_chart,

                width="stretch"
            )

        except Exception as e:

            st.warning(
                f"""
Histogram visualization skipped:

{e}
"""
            )

    # =====================================
    # PIE CHART
    # =====================================

    with chart_col2:

        categorical_columns = [

            col for col in df.columns

            if (

                df[col].dtype == "object"

                or

                df[col].nunique() < 10
            )
        ]

        if len(categorical_columns) > 0:

            try:

                pie_chart = (
                    generate_pie_chart(

                        df,

                        categorical_columns[0]
                    )
                )

                st.plotly_chart(

                    pie_chart,

                    width="stretch"
                )

            except Exception as e:

                st.warning(
                    f"""
Pie chart skipped:

{e}
"""
                )

        else:

            st.info(
                "No suitable categorical columns detected for pie chart visualization."
            )

    st.divider()

    # =====================================
    # DATASET PREVIEW
    # =====================================

    st.subheader(
        "Dataset Preview"
    )

    preview_df = pd.DataFrame(
        st.session_state["preview"]
    )

    st.dataframe(

        preview_df,

        width="stretch"
    )

    st.divider()

    # =====================================
    # AI ANALYTICS WORKFLOW
    # =====================================

    st.subheader(
        "AI Analytics Workflow"
    )

    action1, action2, action3 = (
        st.columns(3)
    )

    # =====================================
    # RUN ANALYSIS
    # =====================================

    with action1:

        if st.button(
            "Run Analysis",
            width="stretch"
        ):

            result = safe_post_request(

                "https://financegpt-multi-agent-financial.onrender.com/analysis/run",

                json_data={
                    "file_path":
                    st.session_state[
                        "file_path"
                    ]
                }
            )

            if result is not None:

                st.success(
                    "Business analysis completed."
                )

                st.subheader(
                    "Business Insights"
                )

                st.write(
                    result.get(
                        "insights"
                    )
                )

                st.subheader(
                    "Executive Commentary"
                )

                st.write(
                    result.get(
                        "commentary"
                    )
                )

    # =====================================
    # RUN FORECAST
    # =====================================

    with action2:

        if st.button(
            "Run Forecast",
            width="stretch"
        ):

            result = safe_post_request(

                "https://financegpt-multi-agent-financial.onrender.com/forecast/run",

                json_data={
                    "file_path":
                    st.session_state[
                        "file_path"
                    ]
                }
            )

            if result is not None:

                st.success(
                    "Forecasting completed."
                )

                st.subheader(
                    "Forecast Summary"
                )

                st.write(
                    result.get(
                        "summary"
                    )
                )

    # =====================================
    # DETECT ANOMALIES
    # =====================================

    with action3:

        if st.button(
            "Detect Anomalies",
            width="stretch"
        ):

            result = safe_post_request(

                "https://financegpt-multi-agent-financial.onrender.com/anomalies/run",

                json_data={
                    "file_path":
                    st.session_state[
                        "file_path"
                    ]
                }
            )

            if result is not None:

                st.success(
                    "Risk analysis completed."
                )

                st.subheader(
                    "Anomaly Summary"
                )

                st.write(
                    result.get(
                        "summary"
                    )
                )

    st.divider()

    # =====================================
    # QUERY ASSISTANT
    # =====================================

    st.subheader(
        "Financial Query Assistant"
    )

    user_query = st.text_input(
        "Ask financial questions about the dataset"
    )

    if st.button(
        "Submit Query",
        width="stretch"
    ):

        if user_query.strip() == "":

            st.warning(
                "Please enter a financial query."
            )

        else:

            with st.spinner(
                "Generating AI response..."
            ):

                result = safe_post_request(

                    "https://financegpt-multi-agent-financial.onrender.com/query/run",

                    json_data={

                        "query":
                        user_query,

                        "file_path":
                        st.session_state[
                            "file_path"
                        ]
                    }
                )

                if result is not None:

                    st.success(
                        "Query processed successfully."
                    )

                    st.subheader(
                        "AI Response"
                    )

                    st.write(

                        result.get(
                            "response"
                        )
                    )
