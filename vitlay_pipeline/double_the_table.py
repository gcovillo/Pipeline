# Last file
import pandas as pd
from mario import set_schedule

@set_schedule(function = "double_table()",
              runAfter = 'elongate_the_table.py', maxAge = '1hr',
              windowOpen = "mon,tue,wed,thur,sun",
              windowOpenTime = '12:30am',
              runAt = '4pm',
              windowCloseIn = '30min')
def double_table():
    df = pd.read_csv('table.csv')
    df = df*2
    df.to_csv('table.csv', index=False)