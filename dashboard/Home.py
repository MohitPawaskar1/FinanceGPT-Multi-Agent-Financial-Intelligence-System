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


# =====================================
# CONFIG
# =====================================

st.set_page_config(
    page_title="FinanceGPT",
    layout="wide"
)

apply_dashboard_styling()

BACKEND = (
    "https://financegpt-multi-agent-financial.onrender.com"
)


# =====================================
# HEADER
# =====================================

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


# =====================================
# SESSION
# =====================================

defaults = {

    "file_path": None,
    "uploaded_df": None,
    "preview": None,
    "target_info": None

}

for k, v in defaults.items():

    if k not in st.session_state:

        st.session_state[k] = v


# =====================================
# REQUEST
# =====================================

def safe_post(
    url,
    files=None,
    json_data=None
):

    try:

        r = requests.post(
            url,
            files=files,
            json=json_data,
            timeout=120
        )

        if r.status_code != 200:

            st.error(
                f"API Error\n\n{r.text}"
            )

            return None

        return r.json()

    except Exception as e:

        st.error(str(e))

        return None


# =====================================
# UPLOAD
# =====================================

uploaded = st.file_uploader(

    "Upload Dataset",

    type=[
        "csv",
        "xlsx"
    ]
)

if uploaded:

    with st.spinner(
        "Uploading..."
    ):

        try:

            uploaded.seek(0)

            if uploaded.name.endswith(
                ".csv"
            ):

                local_df = (
                    pd.read_csv(
                        uploaded
                    )
                )

            else:

                local_df = (
                    pd.read_excel(
                        uploaded
                    )
                )

            st.session_state[
                "uploaded_df"
            ] = local_df

            st.session_state[
                "preview"
            ] = (
                local_df
                .head(20)
                .to_dict(
                    "records"
                )
            )

            uploaded.seek(0)

            result = safe_post(

                f"{BACKEND}/upload/",

                files={

                    "uploaded_file": (

                        uploaded.name,

                        uploaded,

                        uploaded.type
                    )
                }
            )

            if result:

                st.session_state[
                    "file_path"
                ] = (
                    result.get(
                        "file_path"
                    )
                )

                st.session_state[
                    "target_info"
                ] = (
                    result.get(
                        "target_info"
                    )
                )

                st.success(
                    "Dataset uploaded successfully."
                )

        except Exception as e:

            st.error(str(e))


# =====================================
# DASHBOARD
# =====================================

if st.session_state[
    "uploaded_df"
] is not None:

    try:

        df = (
            st.session_state[
                "uploaded_df"
            ]
        )

        df = (
            preprocess_financial_data(
                df
            )
        )

    except Exception:

        st.warning(
            "Upload dataset again."
        )

        st.stop()

    target = None

    if (
        st.session_state[
            "target_info"
        ]
        is not None
    ):

        target = (
            st.session_state[
                "target_info"
            ].get(
                "selected_target"
            )
        )

    if (
        target
        not in df.columns
    ):

        numeric = (
            df
            .select_dtypes(
                include="number"
            )
            .columns
        )

        target = (
            numeric[0]
            if len(
                numeric
            )
            else None
        )

    if target:

        kpi = calculate_kpis(
            df,
            target
        )

        st.subheader(
            "Executive KPI Overview"
        )

        c1, c2, c3, c4 = (
            st.columns(4)
        )

        c1.metric(
            "Average",
            kpi[
                "average_value"
            ]
        )

        c2.metric(
            "Maximum",
            kpi[
                "maximum_value"
            ]
        )

        c3.metric(
            "Minimum",
            kpi[
                "minimum_value"
            ]
        )

        c4.metric(
            "Trend",
            kpi[
                "trend_strength"
            ]
        )

        st.divider()

        col1, col2 = (
            st.columns(2)
        )

        with col1:

            try:

                st.plotly_chart(

                    generate_histogram(
                        df,
                        target
                    ),

                    width="stretch"
                )

            except:
                pass

        with col2:

            cats = [

                c

                for c in df.columns

                if (
                    str(
                        df[c]
                        .dtype
                    )
                    ==
                    "object"
                )
            ]

            if cats:

                try:

                    st.plotly_chart(

                        generate_pie_chart(
                            df,
                            cats[0]
                        ),

                        width="stretch"
                    )

                except:
                    pass

        st.divider()

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        df.head(20),
        width="stretch"
    )

    st.divider()

    a1, a2, a3 = (
        st.columns(3)
    )

    with a1:

        if st.button(
            "Run Analysis"
        ):

            result = safe_post(

                f"{BACKEND}/analysis/run",

                json_data={

                    "file_path":
                    st.session_state[
                        "file_path"
                    ]
                }
            )

            if result:

                st.write(
                    result.get(
                        "insights"
                    )
                )

                st.write(
                    result.get(
                        "commentary"
                    )
                )

    with a2:

        if st.button(
            "Run Forecast"
        ):

            result = safe_post(

                f"{BACKEND}/forecast/run",

                json_data={

                    "file_path":
                    st.session_state[
                        "file_path"
                    ]
                }
            )

            if result:

                st.write(
                    result.get(
                        "summary"
                    )
                )

    with a3:

        if st.button(
            "Detect Anomalies"
        ):

            result = safe_post(

                f"{BACKEND}/anomalies/run",

                json_data={

                    "file_path":
                    st.session_state[
                        "file_path"
                    ]
                }
            )

            if result:

                st.write(
                    result.get(
                        "summary"
                    )
                )

    st.divider()

    query = st.text_input(
        "Ask questions"
    )

    if st.button(
        "Submit Query"
    ):

        result = safe_post(

            f"{BACKEND}/query/run",

            json_data={

                "query":
                query,

                "file_path":
                st.session_state[
                    "file_path"
                ]
            }
        )

        if result:

            st.write(
                result.get(
                    "response"
                )
            )
