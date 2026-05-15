from fastapi import FastAPI

from app.api.routes.analysis import (
    router as analysis_router
)

from app.api.routes.forecasting import (
    router as forecasting_router
)

from app.api.routes.anomalies import (
    router as anomalies_router
)

from app.api.routes.query import (
    router as query_router
)


app = FastAPI(
    title="FinanceGPT API",
    version="1.0.0"
)


app.include_router(
    analysis_router
)

app.include_router(
    forecasting_router
)

app.include_router(
    anomalies_router
)

app.include_router(
    query_router
)


@app.get("/")
def root():

    return {
        "message":
        "FinanceGPT API Running"
    }