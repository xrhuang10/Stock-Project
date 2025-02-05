import os
from dotenv import load_dotenv, dotenv_values
import requests
import json
import pandas as pd

load_dotenv()

api_key = os.getenv("tiingo_key")
stock_symbol = "AAPL"

url = f"https://api.tiingo.com/tiingo/daily/{stock_symbol}/prices?startDate=2012-1-1&endDate=2016-1-1"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {api_key}"
}

# Make the request
response = requests.get(url, headers = headers)

if response.status_code == 200:
    data = response.json()

    # Convert list of dictionaries to DataFrame
    dataframe = pd.DataFrame(data)

    # Convert date column to datetime and set as index
    dataframe["date"] = pd.to_datetime(dataframe["date"])
    dataframe.set_index("date", inplace=True)

    # Convert numerical columns to float
    numeric_columns = ["open", "high", "low", "close", "volume"]
    dataframe[numeric_columns] = dataframe[numeric_columns].astype(float)

    # Sort by date
    dataframe = dataframe.sort_index()

print(dataframe)

# # Print DataFrame details
# size = len(dataframe)
# print(dataframe.iloc[1300:1317])  # Print specific rows

# # Get the latest stock price
# latest_time = dataframe.index[-1]  # Get the most recent date
# latest_price = dataframe.loc[latest_time, "1. open"]

# prices = dataframe["4. close"]

# print(f"Latest {stock_symbol} stock price (weekly open): ${latest_price:.2f}")

# print(f"API Key: {api_key}")  # Debugging API key (Remove if sensitive)