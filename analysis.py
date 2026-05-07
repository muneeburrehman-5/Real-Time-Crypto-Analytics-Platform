import pandas as pd
from database import get_connection
def get_data():
    conn = get_connection()

    query = "SELECT * FROM crypto_market"

    df = pd.read_sql(query, conn)

    conn.close()

    return df
def top_gainers():

    conn = get_connection()

    query = """
    SELECT name, price_change_24h
    FROM crypto_market
    ORDER BY price_change_24h DESC
    LIMIT 5
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
def top_market_cap():

    conn = get_connection()

    query = """
    SELECT name, market_cap
    FROM crypto_market
    ORDER BY market_cap DESC
    LIMIT 5
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
def avg_market_cap():

    conn = get_connection()

    query = """
    SELECT AVG(market_cap) AS avg_market_cap
    FROM crypto_market
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
def total_market_value():

    conn = get_connection()

    query = """
    SELECT SUM(market_cap) AS total_market_cap
    FROM crypto_market
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
def most_volatile():

    conn = get_connection()

    query = """
    SELECT name, price_change_24h, total_volume
    FROM crypto_market
    ORDER BY ABS(price_change_24h) DESC
    LIMIT 5
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
if __name__ == "__main__":

    print("Top Gainers")
    print(top_gainers())

    print("Top Market Cap")
    print(top_market_cap())