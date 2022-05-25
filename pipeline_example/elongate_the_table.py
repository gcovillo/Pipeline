# Second file
"""
function elongate_table()
Window-open mon,tue,wed,thur,sun 12:30am
Window-close-in 1hr
run-after create_table.py
"""
import pandas as pd


def elongate_table():
    df = pd.read_csv('table_2.csv')
    df = pd.concat([df,df], ignore_index=False, axis=0)
    df.to_csv('table_2.csv', index=False)