def generate_insights(df):

    print("\nTOP JOB TITLES:")
    print(df["position"].value_counts().head(10))

    print("\nTOP LOCATIONS:")
    print(df["location"].value_counts().head(10))