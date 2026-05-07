import psycopg2

def get_connection():

    conn = psycopg2.connect(
        host="ep-orange-glitter-aq8wpv2j-pooler.c-8.us-east-1.aws.neon.tech",
        database="crypto_db",
        user="neondb_owner",
        password="npg_yOkZf1E5RAeP",
        port="5432",
        sslmode="require"
    )

    return conn


def create_table():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS crypto_market(
        id SERIAL PRIMARY KEY,
        coin_id TEXT,
        symbol TEXT,
        name TEXT,
        current_price FLOAT,
        market_cap BIGINT,
        total_volume BIGINT,
        price_change_24h FLOAT,
        market_cap_rank INTEGER,
        extracted_at TIMESTAMP,
        volatility_score FLOAT
    );
    """)

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":

    create_table()

    print("Table created successfully")