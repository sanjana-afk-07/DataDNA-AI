import pandas as pd


def calculate_similarity(file1, file2):
    """Calculate similarity between two datasets."""

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    columns1 = set(df1.select_dtypes(include="number").columns)
    columns2 = set(df2.select_dtypes(include="number").columns)

    common_columns = list(columns1.intersection(columns2))

    if not common_columns:
        return {
            "similarity_score": 0,
            "message": "No common numeric columns found."
        }

    scores = []

    for column in common_columns:
        mean1 = df1[column].mean()
        mean2 = df2[column].mean()

        max_mean = max(abs(mean1), abs(mean2), 1)

        difference = abs(mean1 - mean2)

        similarity = max(
            0,
            1 - (difference / max_mean)
        )

        scores.append(similarity)

    final_score = round(
        (sum(scores) / len(scores)) * 100,
        2
    )

    return {
        "common_columns": common_columns,
        "similarity_score": final_score
    }
