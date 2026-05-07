import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("🚀 Real-Time Crypto Analytics")

conn = get_connection()

query = "SELECT * FROM crypto_market ORDER BY extracted_at DESC"

df = pd.read_sql(query, conn)

conn.close()

st.subheader("Latest Data")
st.dataframe(df)

st.subheader("Market Cap Chart")
st.bar_chart(df.set_index("name")["market_cap"])

st.subheader("Price Change 24h")
st.bar_chart(df.set_index("name")["price_change_24h"])