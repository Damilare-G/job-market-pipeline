from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load processed dataset
df = pd.read_csv("data/jobs.csv")


@app.get("/")
def home():
    return {
        "message": "Job Market ETL API is running"
    }


@app.get("/jobs")
def get_jobs():
    return df.head(20).to_dict(orient="records")


@app.get("/jobs/count")
def job_count():
    return {
        "total_jobs": len(df)
    }


@app.get("/locations")
def top_locations():
    locations = (
        df["location"]
        .value_counts()
        .head(10)
        .to_dict()
    )

    return locations