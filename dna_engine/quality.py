import pandas as pd


def analyze_quality(file_path):
    """Analyze the quality of a dataset."""

    df = pd.read_csv(file_path)

    total_cells = df.shape[0] * df.shape[1]

    missing_cells = int(df.isnull().sum().sum())
    duplicate_rows = int(df.duplicated().sum())

    missing_percentage = 0

    if total_cells > 0:
        missing_percentage = round(
            (missing_cells / total_cells) * 100, 2
        )

    if missing_percentage == 0 and duplicate_rows == 0:
        quality_status = "Excellent"

    elif missing_percentage <= 5 and duplicate_rows <= 2:
        quality_status = "Good"

    elif missing_percentage <= 20:
        quality_status = "Needs Cleaning"

    else:
        quality_status = "Poor"

    return {
        "missing_cells": missing_cells,
        "missing_percentage": missing_percentage,
        "duplicate_rows": duplicate_rows,
        "quality_status": quality_status
    }
