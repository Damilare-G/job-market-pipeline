import sqlite3


def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


def save_to_sqlite(df, db_name, table_name):
    conn = sqlite3.connect(db_name)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print(f"Data saved to database: {db_name}")