# Second file
"""
function elongate_table()
Window-open mon,tue,wed,thur,sun 12:30am
Window-close-in 1hr
run-after create_table.py
"""
import pandas as pd


def elongate_table():
<<<<<<< HEAD
    df = pd.read_csv('table.csv')
    df = pd.concat([df,df], ignore_index=True, axis=0)
    df.to_csv('table.csv', index=False)
=======
    df = pd.read_csv('table_1.csv')
    df = pd.concat([df,df], ignore_index=False, axis=0)
    df.to_csv('table_1.csv', index=False)
>>>>>>> 3642a81d9d47990508e084331c3b2f9593a51f99
