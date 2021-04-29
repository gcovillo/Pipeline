"""
CTRL-M main()
Window-open mon,tue,wed,thur,fri,sat,sun 11pm
Window-close-in 1hr
run-at None
"""


import pandas as pd
from polygon import RESTClient
from IPython.display import display
import datetime
def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')

def main():
    x = 'this is fake'
    b = 'this is just to test'
    os.system('cp outputs/stockData.csv stockData.csv')
