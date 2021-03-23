""" 
CTRL-M main()
Window-open mon,tue,wed,thur,fri,sat,sun 11pm
Window-close-in 1h
"""

import pandas as pd
from polygon import RESTClient
from IPython.display import display
import datetime
def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main():
    key = 'Evy8nViLZhZNYgsyU13tSrtn42qRTKci'

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    dt, o, h, l, c, v, vw = [], [], [], [], [], [], []
    with RESTClient(key) as client:
        from_ = "2019-02-01"
        to = "2021-02-10"
        resp = client.stocks_equities_aggregates("AAPL", 1, "minute", from_, to, unadjusted=True)
        print(f"Minute aggregates for {resp.ticker} between {from_} and {to}.")
        for result in resp.results:
            dt.append(ts_to_datetime(result["t"]))
            o.append(result['o'])
            h.append(result['h'])
            l.append(result['l'])
            c.append(result['c'])
            v.append(result['v'])
            vw.append(result['vw'])

            
        df = pd.DataFrame(list(zip(dt, o, h, l, c, v, vw)), 
                          columns = ["Date", "Open Price", "Highest Price", "Lowest Price", "Close Price", "Trading Volume", 'Volume Weighted Average Price'])
        df['Date']= pd.to_datetime(df['Date'])
        df.to_csv('stockData.csv')
        
        return True
