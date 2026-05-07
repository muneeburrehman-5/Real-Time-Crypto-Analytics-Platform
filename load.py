from database import get_connection

def load(df):

    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
       cur.execute("""
INSERT INTO crypto_market
(coin_id, symbol, name, current_price, market_cap, total_volume,
 price_change_24h, market_cap_rank, extracted_at, volatility_score)

VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
""", tuple(row))

    conn.commit()
    cur.close()
    conn.close()