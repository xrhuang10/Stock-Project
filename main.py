import os
from dotenv import load_dotenv, dotenv_values
import requests
import json
import pandas as pd
import numpy as np

load_dotenv()

api_key = os.getenv("tiingo_key")
stock_symbol = "TSLA"
regression_type = "random_forest"

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

training_data = dataframe["high"].values
print(training_data)

export_csv = dataframe.to_csv (r'export_dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

