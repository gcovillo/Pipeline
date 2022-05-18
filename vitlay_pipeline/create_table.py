# First file
"""
function create_table()
Window-open mon,tue,wed,thur,sun
Window-close-in 1hr
group_name vitaly_test_group
owner Vitaly Pankratov
pipeline = table
"""

import pandas as pd
import time


def create_table():
    data = [[1,2],[3,4], [5,6]]
    columns = ['A', 'B']

    df = pd.DataFrame(data, columns=columns)
    df.to_csv('table.csv', index=False)
    time.sleep(120)