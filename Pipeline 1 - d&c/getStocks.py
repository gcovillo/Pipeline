""" 
function main()
Window-open mon,tue,wed,thur,fri,sat 11pm
Window-close-in 1h
dont-run-time ['11:30pm']
group_name stock_pipelines
owner Gillian Covillo
pipeline = 'gillians_stocks'
"""

import pandas as pd
from polygon import RESTClient
from IPython.display import display
import datetime
from yahoo_fin.stock_info import get_data

def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')

def main():

    # Random Log File
    file1 = open("log.txt", "a")  # append mode
    file1.write("This is a log file")
    file1.write("loggy  the log log")
    file1.close()

    df = get_data("AAPL", start_date="02/10/2019", end_date="2/20/2021", index_as_date=True, interval="1d")
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Date', 'open': 'Open Price', 'high': 'Highest Price', 'low': "Lowest Price", 'close': 'Close Price', 'adjclose': 'Trading Volume', 'volume': 'Volume Weighted Average Price'}, inplace=True)


    df.to_csv('stockData.csv')
        
 
