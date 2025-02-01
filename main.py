import os
from dotenv import load_dotenv, dotenv_values
import requests
import json
import pandas as pd

load_dotenv()

api_key = os.getenv("alpha_vantage_key")
stock_symbol = "AAPL"

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={stock_symbol}&apikey={api_key}"

# Make the request
response = requests.get(url)

# Convert to JSON
data = response.json()

time_series = data.get("Weekly Time Series", {})

# Convert to DataFrame
dataframe = pd.DataFrame.from_dict(time_series, orient="index")
dataframe = dataframe.astype(float)  # Convert values to numeric
dataframe.index = pd.to_datetime(dataframe.index)  # Convert index to datetime
dataframe = dataframe.sort_index()  # Sort by date

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