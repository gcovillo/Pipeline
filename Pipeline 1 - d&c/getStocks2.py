import pandas as pd
from polygon import RESTClient
from IPython.display import display
import datetime
from yahoo_fin.stock_info import get_data
from mario import set_schedule

def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')

@set_schedule('stockData.csv',
              function="main()",
              runAfter='QA_stocks.py', maxAge='1hr',
              windowOpen="['mon','wed','fri','sun']",
              windowOpenTime='4am',
              windowCloseIn='1hr',
              runAt='4am'
              )
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
        
 
