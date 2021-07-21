import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
import numpy as np
import datetime
import warnings
from mario import set_schedule
warnings.filterwarnings("ignore")


@set_schedule('stockData.csv',
              function = "createTS('stockData.csv')",
              runAfter = 'QA_stocks.py', maxAge = '1hr', 
              windowOpen = "['mon','wed','fri','sun']",
              windowOpenTime = '4am',
              windowCloseIn = '1hr',
             runAt = '4am')
def createTS(data):
    data = pd.read_csv(data)
    data.dropna(inplace=True)
    df_close = data['Close Price']
    df_log = np.log(df_close)
    train_data, test_data = df_log[3:int(len(df_log)*0.85)], df_log[int(len(df_log)*0.85):]
    model = ARIMA(train_data, order=(3, 1, 2))
    fitted = model.fit(disp=0)
    forecasts = fitted.forecast(steps=30)
    days = []
    closes = []
    for i, item in enumerate(forecasts[0]):
        days.append(data.at[len(data)-1, 'Date'] + str(datetime.timedelta(days=i+1)))
        closes.append(np.exp(item))
    df = pd.DataFrame(list(zip(days,closes)), columns = ['Date', 'Close Price'])
    df2 = data[['Date', 'Close Price']].copy(deep=True)
    df3 = df2.append(df)

    df3.to_csv('TSData.csv')


