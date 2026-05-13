from pathlib import Path

SUPPORTED_FILE_TYPES = [".csv", ".xlsx"]


def validate_file_path(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix not in SUPPORTED_FILE_TYPES:
        raise ValueError(
            f"Unsupported file type: {path.suffix}"
        )

    return True