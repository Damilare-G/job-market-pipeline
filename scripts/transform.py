import pandas as pd


def clean_jobs(df):
    """
    Cleans and transforms raw job data.
    """

    # Select important columns
    selected_columns = [
        "company",
        "position",
        "location",
        "tags",
        "salary_min",
        "salary_max",
        "date"
    ]

    # Keep only existing columns
    existing_columns = [
        col for col in selected_columns
        if col in df.columns
    ]

    df = df[existing_columns]

    # Convert lists in tags column to strings
    if "tags" in df.columns:
        df["tags"] = df["tags"].apply(
            lambda x: ", ".join(x) if isinstance(x, list) else str(x)
        )

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("Not Specified")

    return df


if __name__ == "__main__":
    print("Transform module ready.")