# Job Market ETL Pipeline
A Python-based ETL pipeline that extracts real-time tech job listings from an external API, transforms and cleans the data, and stores it in CSV and SQLite formats for analytics and reporting.

## Features
- Extracts job data from a public API
- Cleans and transforms raw datasets
- Removes duplicates and handles missing values
- Stores processed data in:
  - CSV
  - SQLite database
- Generates basic analytics and insights
- Modular ETL architecture
- Git version control
- Docker-ready structure

## Tech Stack
- Python
- Pandas
- Requests
- SQLite
- Git/GitHub
- Docker

## Project Structure
```plaintext
job-market-pipeline/
│
├── data/
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── analyze.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run
1. Clone the repository
2. Create virtual environment
3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run pipeline

```bash
python main.py
```

## Future Improvements
- Docker containerization
- PostgreSQL integration
- FastAPI endpoint
- Automated scheduling
- Dashboard visualizations

## API Extension

The project includes a FastAPI-based API layer (`api.py`) for exposing processed job-market data through REST endpoints.

Endpoints include:
- `/jobs`
- `/jobs/count`
- `/locations`

Note: Running FastAPI locally may require adjusting Windows security or application control policies depending on the system environment.