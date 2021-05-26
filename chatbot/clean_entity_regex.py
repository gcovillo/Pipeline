"""
CTRL-M clean_entity_regex()
Window-open mon,tue,wed,thur,fri,sat,sun 12:30am
Window-close-in 1hr
run-after clean_entity_dict.py
run-at None
"""

import pandas as pd
import os


def clean_entity_regex():
    regex = []
    folder_path = "data/raw/v001/Entity Data/"
    folder = os.listdir(folder_path)
    for file in folder:
        if 'regex' in file:
            regex.append(file)

    entity_names = []
    regex_arrays = []

    for file in regex:
        entity_name = file.replace("EN_RB_ANY_ANY_", "").replace("_regex", "")
        folder_path = "data/raw/v001/Entity Data/"
        path = folder_path + file
        entity_file = open(path, "r")
        temp_array = []
        for line in entity_file:
            temp_array.append(line.replace("\n", ""))

        entity_names.append(entity_name)
        regex_arrays.append(temp_array)

    regex_df = pd.DataFrame({'Entityname': entity_names,
                             'regex_array': regex_arrays})

    regex_df.to_csv('entity_regex.csv')
