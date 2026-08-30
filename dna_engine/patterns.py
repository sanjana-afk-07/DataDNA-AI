import pandas as pd


def discover_patterns(file_path):
    """Find strong relationships between numeric columns."""

    df = pd.read_csv(file_path)

    numeric_data = df.select_dtypes(include="number")

    if numeric_data.shape[1] < 2:
        return {
            "message": "Not enough numeric columns to discover patterns."
        }

    correlation = numeric_data.corr()

    patterns = []

    columns = correlation.columns

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            value = correlation.iloc[i, j]

            if abs(value) >= 0.7:
                patterns.append({
                    "feature_1": columns[i],
                    "feature_2": columns[j],
                    "correlation": round(float(value), 2),
                    "strength": "Strong"
                })

    return {
        "strong_relationships": patterns
    }
