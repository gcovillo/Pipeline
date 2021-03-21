"""
CTRL-M send2db(df)
Window-open sun 4am
Window-close-in 1h
"""

import mympsql

def send2db(data):
    connection = pymysql.connect(host='localhost',
                                 user = 'sampleUser',
                                 password = 'pass',
                                 db = 'forecasts')
    cursor = connection.cursor()

    sql = "INSERT INTO 'forecasts' ('Date', 'Predicted Close') VALUES (%s, %s)"

    for i in range(len(data)):
        cursor.execute(sql, (data.at[i, 'Date'], data.at[i, 'close']))
        connection.commit()
    
    connection.close()
    
    return True

