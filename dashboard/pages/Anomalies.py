import streamlit as st
import requests
import pandas as pd


st.title("Anomaly Detection")

st.markdown("""
Detect unusual financial behavior patterns.
""")

if st.button(
    "Run Anomaly Detection"
):

    with st.spinner(
        "Detecting anomalies..."
    ):

        response = requests.post(
            "http://127.0.0.1:8000/anomalies/run"
        )

        result = response.json()

    anomaly_df = pd.DataFrame(
        result["results"]
    )

    st.subheader("Detection Results")

    st.dataframe(
        anomaly_df,
        use_container_width=True
    )

    st.subheader("Summary")

    st.write(result["summary"])