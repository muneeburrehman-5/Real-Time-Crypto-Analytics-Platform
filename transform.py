import pandas as pd
from datetime import datetime

def transform(data):

    # convert API data into dataframe
    df = pd.DataFrame(data)

    # select original API columns
    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h",
        "market_cap_rank"
    ]]

    # remove missing values
    df = df.dropna()

    # create volatility score
    df["volatility_score"] = (
        abs(df["price_change_percentage_24h"])
        * df["total_volume"]
    )

    # add extraction timestamp
    df["extracted_at"] = datetime.utcnow()

    # rename columns
    df.rename(columns={
        "id": "coin_id",
        "price_change_percentage_24h": "price_change_24h"
    }, inplace=True)

    # final correct column order
    df = df[[
        "coin_id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_24h",
        "market_cap_rank",
        "extracted_at",
        "volatility_score"
    ]]

    return df