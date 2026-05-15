import streamlit as st
import requests


st.title("Financial Analysis")

st.markdown("""
Run AI-powered financial analysis workflows.
""")

if st.button("Run Analysis"):

    with st.spinner(
        "Running analysis workflow..."
    ):

        response = requests.post(
            "http://127.0.0.1:8000/analysis/run"
        )

        result = response.json()

    st.success("Analysis completed.")

    if result.get("insights"):

        st.subheader("Insights")

        st.write(result["insights"])

    if result.get("commentary"):

        st.subheader("AI Commentary")

        st.write(result["commentary"])