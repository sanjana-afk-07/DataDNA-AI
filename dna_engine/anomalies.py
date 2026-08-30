import pandas as pd


def detect_anomalies(file_path):
    """Detect unusual values using the IQR method."""

    df = pd.read_csv(file_path)
    numeric_columns = df.select_dtypes(include="number").columns

    anomalies = {}

    for column in numeric_columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower_limit = q1 - (1.5 * iqr)
        upper_limit = q3 + (1.5 * iqr)

        count = int(
            ((df[column] < lower_limit) |
             (df[column] > upper_limit)).sum()
        )

        anomalies[column] = count

    return anomalies
