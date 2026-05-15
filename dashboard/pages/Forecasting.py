import streamlit as st
import requests
import pandas as pd
import plotly.express as px


st.title("Forecasting")

st.markdown("""
Financial trend forecasting engine.
""")

if st.button("Generate Forecast"):

    with st.spinner(
        "Generating forecast..."
    ):

        response = requests.post(
            "http://127.0.0.1:8000/forecast/run"
        )

        result = response.json()

    forecast_df = pd.DataFrame(
        result["forecast"]
    )

    st.subheader("Forecast Results")

    st.dataframe(
        forecast_df,
        use_container_width=True
    )

    fig = px.line(
        forecast_df,
        x="time_index",
        y="forecast",
        markers=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Forecast Summary")

    st.write(result["summary"])