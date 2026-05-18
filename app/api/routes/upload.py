import os

import pandas as pd

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.data.loader import (
    load_financial_data
)

from app.data.preprocessing import (
    preprocess_financial_data
)

from app.intelligence.column_detector import (
    detect_date_columns,
    detect_numeric_targets
)

from app.intelligence.target_selector import (
    select_forecast_target
)


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


UPLOAD_DIR = "uploads"


@router.post("/")
async def upload_dataset(
    uploaded_file: UploadFile = File(...)
):

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True
    )

    file_path = os.path.join(
        UPLOAD_DIR,
        uploaded_file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        content = await uploaded_file.read()

        f.write(content)

    df = load_financial_data(
        file_path
    )

    df = preprocess_financial_data(df)

    date_columns = (
        detect_date_columns(df)
    )

    numeric_columns = (
        detect_numeric_targets(df)
    )

    target_info = (
        select_forecast_target(
            df,
            numeric_columns
        )
    )

    preview = df.head(10).to_dict(
        orient="records"
    )

    return {

        "file_path":
        file_path,

        "columns":
        df.columns.tolist(),

        "shape":
        df.shape,

        "preview":
        preview,

        "date_columns":
        date_columns,

        "numeric_columns":
        numeric_columns,

        "target_info":
        target_info
    }