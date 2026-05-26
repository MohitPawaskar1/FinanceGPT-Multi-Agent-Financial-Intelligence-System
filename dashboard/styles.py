import streamlit as st


def apply_dashboard_styling():

    st.markdown(
        """

<style>

/* Main Background */

.main {

    background-color: #f5f7fb;
}


/* Metric Cards */

[data-testid="metric-container"] {

    background-color: white;

    border-radius: 14px;

    padding: 14px;

    border: 1px solid #e5e7eb;

    box-shadow:
    0 1px 3px rgba(0,0,0,0.05);
}


/* Section Containers */

.block-container {

    padding-top: 2rem;

    padding-bottom: 2rem;
}


/* Chart Containers */

.stPlotlyChart {

    background-color: white;

    border-radius: 14px;

    padding: 10px;

    border: 1px solid #e5e7eb;
}


/* Buttons */

.stButton > button {

    border-radius: 10px;

    border: none;

    background-color: #2563eb;

    color: white;

    font-weight: 600;
}


/* Text Inputs */

.stTextInput > div > div > input {

    border-radius: 10px;
}

</style>

        """,

        unsafe_allow_html=True
    )