# Last file
import pandas as pd
from mario import set_schedule

@set_schedule(function = "double_table(coef)",
              runAfter = 'elongate_the_table.py', maxAge = '1hr',
              windowOpen = "mon,tue,wed,thur,sun",
              windowOpenTime = '12:30am',
              runAt = '4pm',
              windowCloseIn = '30min')
def double_table(coef):
    df = pd.read_csv('table_2.csv')
    df = df*int(coef)
    df.to_csv('output.csv', index=False)