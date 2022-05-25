# First file
"""
function create_table()
Window-open mon,tue,wed,thur,sun
Window-close-in 1hr
group_name vitaly_test_group
owner Vitaly Pankratov
pipeline = 'test_3_25_05_2022'
"""
import pandas as pd
def create_table():
    data = [[1,2],[3,4], [5,6], [7,8],[9,10]]
    columns = ['A', 'B']

    df = pd.DataFrame(data, columns=columns)
    df.to_csv('table_2.csv', index=False)
