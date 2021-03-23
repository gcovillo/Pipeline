import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
import numpy as np
import datetime
from mario import set_schedule 

@set_schedule(df, 
             CTRLM = 'createTS(df)', 
             runAfter = 'QA_stocks.py', maxAge = '2hr', 
             windowOpen = '[sun]', 
             windowOpenTime = '3am', 
             widowCloseIn = '1hr')
def createTS(data):
    df_close = data['close']
    df_log = np.log(df_close)
    train_data, test_data = df_log[3:int(len(df_log)*0.85)], df_log[int(len(df_log)*0.85):]
    model = ARIMA(train_data, order=(3, 1, 2))  
    fitted = model.fit(disp=-1)  
    forecasts = fitted.forecast(steps=30)
    days = []
    closes = []
    for i, item in enumerate(forecasts[0]):
        days.append(data.at[len(data)-1, 'Date'] + datetime.timedelta(days=i+1))
        closes.append(np.exp(item))
    df = pd.DataFrame(list(zip(days,closes)), columns = ['Date', 'close'])
    df2 = data[['Date', 'close']].copy(deep=True)
    return df2.append(df)
