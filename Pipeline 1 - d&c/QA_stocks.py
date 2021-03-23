import pandas as pd
from IPython.display import display, clear_output
from pandas_profiling import ProfileReport
from yahoo_fin.stock_info import get_data 
import numpy as np
from mario import set_schedule


apple_daily= get_data("AAPL", start_date="02/10/2019", end_date="2/20/2021", index_as_date = True, interval="1d")
apple_daily.reset_index(inplace=True)
apple_daily.rename(columns={'index':'Date'}, inplace=True)

def isComplete(data):
    return pd.isnull(data).any().any()

def isUnique(data):
    return data.all().all() == data.drop_duplicates().all().all()

def isValid(data):
    if (len(data['Date'].map(type).unique()) != 1):
        return False
    else:
        return True
        #types = [pd._libs.tslibs.timestamps.Timestamp, float64, np.float64, np.float64, np.float64, np.float64, np.float64]
        #for i, col in enumerate(data.columns):
            #if type(data.at[col, 3]) != types[i]:
                #return False

def isConsistent(df, apple_daily):
    d, o, h, l, c, v, _ = df.columns
    d2, o2, h2, l2, c2, _, v2, _ = apple_daily.columns
    for r in range(df.shape[0]):
        for r2 in range(apple_daily.shape[0]):
            if df.at[r, d] == apple_daily.at[r2, d2]:
                foundDateMatch = True
                if ((df.at[r, o] != apple_daily.at[r2, o2]) or (df.at[r, h] != apple_daily.at[r2, h2]) or (df.at[r, l] != apple_daily.at[r2, l2]) or (df.at[r, c] != apple_daily.at[r2, c2]) or (df.at[r, v] != apple_daily.at[r2, v2])):
                    return False
    return True

def completeData(data):
    return data.dropna().copy(deep=True)
    #should add a method to impute the data

def uniqueData(data):
    return data.drop_duplicates().copy(deep=True)

def ValidateColumns(data):
    try:
        data['Date'] = pd.to_datetime(data['Date'])
        data['Open Price'] = pd.to_numeric(data['Open Price'])
        data['Highest Price'] = pd.to_numeric(data['Highest Price'])
        data['Lowest Price'] = pd.to_numeric(data['Lowest Price'])
        data['Close Price'] = pd.to_numeric(data['Close Price'])
        data['Trading Volume'] = pd.to_numeric(data['Trading Price'])
        data['Volume Weighted Average Price'] = pd.to_numeric(data['Volume Weighted Average Price'])
        return "none"
    except:
        return "ValidationError"
"""
def consistifyData(data):
    d, o, h, l, c, v, _ = df.columns
    d2, o2, h2, l2, c2, _, v2, _ = apple_daily.columns
    for r in range(df.shape[0]):
        for r2 in range(apple_daily.shape[0]):
            if df.at[r, d] == apple_daily.at[r2, d2]:
                foundDateMatch = True
                if ((df.at[r, o] != apple_daily.at[r2, o2]) or (df.at[r, h] != apple_daily.at[r2, h2]) or (df.at[r, l] != apple_daily.at[r2, l2]) or (df.at[r, c] != apple_daily.at[r2, c2]) or (df.at[r, v] != apple_daily.at[r2, v2])):
"""

@set_schedule('stockData.csv', "qualityCheck('stockData.csv')", 'getStocks.py', '1hr', '[mon,wed,fri,sun]', '2am', '1hr')
def qualityCheck(data):
    data = pd.read_csv(data)
    apple_daily= get_data("AAPL", start_date="02/10/2019", end_date="2/20/2021", index_as_date = True, interval="1d")
    apple_daily.reset_index(inplace=True)
    apple_daily.rename(columns={'index':'Date'}, inplace=True)
    print("Checking if data is complete.....")
    if isComplete(data) != True:
        print("Data contains Null or None Values")
        data = completeData(data)
        print("Data has been dropped where missing")
    else:
        print("Data is complete")
    
    
    print("Checking if data is unique.....")
    if isUnique(data) !=True:
        print("Data contains non-unique rows")
        data = uniqueData(data)
        print("Duplicate rows have been removed")
    else:
        print("Data is Unique")
    
    print("Checking is data is valid.....")
    if isValid(data) != True:
        print("Data contains inconsistent types amongst columns")
        print("The data may not be valid")
        error = ValidateColumns(data)
        if error == "none":
            print("Data now has consistent types amongst columns")
        else:
            print("Validation issue could not be fixed")
    else:
        print("Data is Valid")

    print("Checking is data is consistent with other sources.....")
    if isConsistent(data, apple_daily)!= True:
        print("Inconsistencies were found in the data")
    
    return True
