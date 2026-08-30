import pandas as pd


def generate_fingerprint(file_path):
    """Generate a basic DataDNA fingerprint for a dataset."""

    df = pd.read_csv(file_path)

    fingerprint = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "numeric_columns": list(df.select_dtypes(include="number").columns),
        "categorical_columns": list(
            df.select_dtypes(exclude="number").columns
        ),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum())
    }

    return fingerprint
