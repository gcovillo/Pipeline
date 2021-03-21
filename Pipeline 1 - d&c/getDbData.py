"""
CTRL-M fetch_from_db()
Window-open mon,wed,fri,sun 2am
Window-close-in 1hr
"""

import pymysql

def fetch_from_db():
    connection = pymysql.connect(host='localhost',
                                 user = 'sampleUser',
                                 password = 'pass',
                                 db = 'apple_stocks')
    cursor = connection.cursor()

    cur.execute('SELECT * FROM forecasts')
    
    df = DataFrame(cur.fetchall())
    
    df.columms = cur.keys()
    
    connection.close()
    
    return df
