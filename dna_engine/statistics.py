import pandas as pd


def calculate_statistics(file_path):
    """Calculate basic statistical DNA of a dataset."""

    df = pd.read_csv(file_path)

    numeric_data = df.select_dtypes(include="number")

    statistics = {
        "mean": numeric_data.mean().round(2).to_dict(),
        "median": numeric_data.median().round(2).to_dict(),
        "standard_deviation": numeric_data.std().round(2).to_dict(),
        "minimum": numeric_data.min().to_dict(),
        "maximum": numeric_data.max().to_dict()
    }

    return statistics
