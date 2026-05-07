Real-Time Crypto Analytics Platform

🚀 A Real-Time Crypto Analytics Platform built using Python, PostgreSQL, Streamlit, and ETL pipelines.
This project extracts live cryptocurrency market data from the CoinGecko API, transforms it using Pandas, stores it in PostgreSQL, and visualizes real-time insights through an interactive Streamlit dashboard.

📌 Features:

Real-time cryptocurrency market analytics
Automated ETL pipeline
Live data extraction from CoinGecko API
PostgreSQL database integration
Data transformation using Pandas
Interactive Streamlit dashboard
Market cap analysis
Top gainers tracking
Volatility analysis
Automated scheduling using APScheduler
🛠️ Tech Stack
Python
Pandas
PostgreSQL
Streamlit
APScheduler
Psycopg2
CoinGecko API

📂 Project Structure:
Real-Time-Crypto-Analytics-Platform/
│
├── database.py
├── extract.py
├── transform.py
├── load.py
├── etl_pipeline.py
├── analysis.py
├── dashboard.py
├── requirements.txt
└── data/
    └── raw.json
    
⚙️ How the Project Works:
1️⃣ Extract:

The project fetches live cryptocurrency data from the CoinGecko API.

File:

extract.py

2️⃣ Transform:

The raw API data is cleaned and transformed using Pandas.

Operations performed:

Selecting required columns,
Removing null values,
Renaming columns,
Creating volatility score,
Adding extraction timestamp,

File:

transform.py

3️⃣ Load:

The transformed data is inserted into a PostgreSQL database.

File:

load.py

4️⃣ ETL Automation:

The ETL pipeline automatically runs every 5 minutes using APScheduler.

File:

etl_pipeline.py

5️⃣ Dashboard

The Streamlit dashboard visualizes:

Latest crypto data
Market cap analysis
Price change analysis
Real-time updates

File:

dashboard.py

🗄️ Database Schema:

Table Name:

crypto_market

Columns:

Column Name	Data Type
id	SERIAL PRIMARY KEY
coin_id	TEXT
symbol	TEXT
name	TEXT
current_price	FLOAT
market_cap	BIGINT
total_volume	BIGINT
price_change_24h	FLOAT
market_cap_rank	INTEGER
extracted_at	TIMESTAMP
volatility_score	FLOAT

🚀 Installation & Setup:
Step 1 — Clone Repository
git clone https://github.com/your-username/Real-Time-Crypto-Analytics-Platform.git
Step 2 — Open Project Folder
cd Real-Time-Crypto-Analytics-Platform
Step 3 — Install Dependencies
pip install -r requirements.txt

🐘 PostgreSQL Setup:

Create a PostgreSQL database named:

crypto_db

Update your database credentials inside:

database.py

Example:

conn = psycopg2.connect(
    host="localhost",
    database="crypto_db",
    user="postgres",
    password="your_password",
    port="5432"
)
▶️ Running the Project:
Create Table
python database.py
Run ETL Pipeline
python etl_pipeline.py
Run Dashboard
streamlit run dashboard.py

📊 Dashboard Preview:

The dashboard displays:

Real-time crypto analytics
Market cap visualization
Price change charts
Updated cryptocurrency records

🌐 API Used:

CoinGecko API

https://api.coingecko.com/api/v3/coins/markets
📚 Key Learnings

This project helped in learning:

ETL pipeline development,
API integration,
PostgreSQL database management,
Data cleaning & transformation,
Streamlit dashboard development,
Real-time analytics,
Python automation,
Cloud deployment basics,
🔥 Future Improvements,
Add machine learning predictions,
Deploy ETL pipeline on cloud server,
Add user authentication,
Add advanced crypto analytics,
Add live websocket streaming,
Dockerize the project,

👨‍💻 Author
Muhammad Muneeb ur Rehman

⭐ If you like this project

Give this repository a ⭐ on GitHub!
