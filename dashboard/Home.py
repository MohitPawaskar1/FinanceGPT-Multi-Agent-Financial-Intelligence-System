import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="FinanceGPT",
    layout="wide"
)

st.title("FinanceGPT")

st.markdown("""
AI-Powered Financial Intelligence Platform
""")

st.divider()

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

        response = requests.post(
            "http://127.0.0.1:8000/upload/",
            files=files
        )

        result = response.json()

        # Session storage

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

        st.session_state["date_columns"] = (
            result["date_columns"]
        )

        st.session_state["numeric_columns"] = (
            result["numeric_columns"]
        )

    st.success(
        "Dataset uploaded successfully."
    )

# =========================================
# ACTIVE DATASET
# =========================================

if "file_path" in st.session_state:

    st.divider()

    st.success(
        f"""
Active Dataset:
{st.session_state['file_path']}
"""
    )

    # =====================================
    # DATASET OVERVIEW
    # =====================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Dataset Shape")

        st.write(
            st.session_state["shape"]
        )

    with col2:

        st.subheader(
            "Detected Date Columns"
        )

        st.write(
            st.session_state[
                "date_columns"
            ]
        )

    st.divider()

    # =====================================
    # TARGET INTELLIGENCE
    # =====================================

    target_info = (
        st.session_state[
            "target_info"
        ]
    )

    st.subheader(
        "Forecast Target Intelligence"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            label="Selected Target",
            value=target_info[
                "selected_target"
            ]
        )

    with col2:

        st.metric(
            label="Confidence",
            value=target_info[
                "confidence"
            ]
        )

    st.subheader(
        "Alternative Targets"
    )

    st.write(
        target_info["top_targets"]
    )

    st.divider()

    # =====================================
    # DATASET PREVIEW
    # =====================================

    st.subheader("Dataset Preview")

    preview_df = pd.DataFrame(
        st.session_state["preview"]
    )

    st.dataframe(
        preview_df,
        use_container_width=True
    )

    st.divider()

    # =====================================
    # AI WORKFLOW ACTIONS
    # =====================================

    st.subheader(
        "AI Workflow Actions"
    )

    col1, col2, col3 = st.columns(3)

    # -------------------------------------
    # ANALYSIS
    # -------------------------------------

    with col1:

        if st.button(
            "Run Analysis",
            use_container_width=True
        ):

            with st.spinner(
                "Running analysis..."
            ):

                response = requests.post(
                    "http://127.0.0.1:8000/analysis/run",
                    json={

                        "file_path":
                        st.session_state[
                            "file_path"
                        ]
                    }
                )

                analysis_result = (
                    response.json()
                )

            st.subheader("Insights")

            st.write(
                analysis_result.get(
                    "insights"
                )
            )

            st.subheader(
                "AI Commentary"
            )

            st.write(
                analysis_result.get(
                    "commentary"
                )
            )

    # -------------------------------------
    # FORECASTING
    # -------------------------------------

    with col2:

        if st.button(
            "Run Forecasting",
            use_container_width=True
        ):

            with st.spinner(
                "Generating forecast..."
            ):

                response = requests.post(
                    "http://127.0.0.1:8000/forecast/run",
                    json={

                        "file_path":
                        st.session_state[
                            "file_path"
                        ]
                    }
                )

                forecast_result = (
                    response.json()
                )

            st.subheader(
                "Forecast Summary"
            )

            st.write(
                forecast_result.get(
                    "summary"
                )
            )

    # -------------------------------------
    # ANOMALY DETECTION
    # -------------------------------------

    with col3:

        if st.button(
            "Detect Anomalies",
            use_container_width=True
        ):

            with st.spinner(
                "Detecting anomalies..."
            ):

                response = requests.post(
                    "http://127.0.0.1:8000/anomalies/run",
                    json={

                        "file_path":
                        st.session_state[
                            "file_path"
                        ]
                    }
                )

                anomaly_result = (
                    response.json()
                )

            st.subheader(
                "Anomaly Summary"
            )

            st.write(
                anomaly_result.get(
                    "summary"
                )
            )

    st.divider()

    # =====================================
    # AI QUERY ASSISTANT
    # =====================================

    st.subheader(
        "Financial Query Assistant"
    )

    user_query = st.text_input(
        "Ask financial questions about the dataset"
    )

    if st.button(
        "Submit Query"
    ):

        with st.spinner(
            "Generating AI response..."
        ):

            response = requests.post(
                "http://127.0.0.1:8000/query/run",
                json={
                    "query": user_query
                }
            )

            query_result = (
                response.json()
            )

        st.subheader(
            "AI Response"
        )

        st.write(
            query_result.get(
                "response"
            )
        )