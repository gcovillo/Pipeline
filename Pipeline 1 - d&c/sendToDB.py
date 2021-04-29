import mympsql
from mario import setSchedule

@setSchedule(df, CTRLM = 'send2db(df)',
             runAfter = None, maxAge = None,
             windowOpen = '[sun]',
             windowOpenTime = '4am',
             widowCloseIn = '1hr',
             runAt = 'None')
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
