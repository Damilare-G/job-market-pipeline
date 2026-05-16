from scripts.analyze import generate_insights
from scripts.extract import fetch_jobs
from scripts.transform import clean_jobs
from scripts.load import save_to_csv, save_to_sqlite


def run_pipeline():
    print("Fetching job data...")

    raw_df = fetch_jobs()

    if raw_df is not None:
        print("Cleaning data...")

        clean_df = clean_jobs(raw_df)

        print("Saving data...")

        save_to_csv(clean_df, "data/jobs.csv")

        save_to_sqlite(
            clean_df,
            "data/jobs.db",
            "jobs"
        )
        print("Generating insights...")

        generate_insights(clean_df)
        print("Pipeline completed successfully!")

    else:
        print("Pipeline failed.")


if __name__ == "__main__":
    run_pipeline()