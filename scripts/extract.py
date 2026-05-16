import requests
import pandas as pd

API_URL = "https://remoteok.com/api"


def fetch_jobs():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(API_URL, headers=headers)

        if response.status_code == 200:
            data = response.json()

            # Remove metadata entry
            jobs = data[1:]

            df = pd.DataFrame(jobs)

            return df

        else:
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        print(f"Request failed: {e}")
        return None


if __name__ == "__main__":
    df = fetch_jobs()

    if df is not None:
        print(df.head())