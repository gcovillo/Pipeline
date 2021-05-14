"""
CTRL-M clean_trained_entities()
Window-open mon,tue,wed,thur,fri,sat,sun 12:50am
Window-close-in 1hr
run-after clean_entity_regex.py
run-at 1am
"""

import pandas as pd
import os


def clean_trained_entities():
    dicty = {}

    entity_names = []
    values = []

    folder_path = "home/ubuntu/test/data/raw/v001/Entity Data/"
    folder = os.listdir(folder_path)
    for file in folder:
        if 'samples' in file:
            path = folder_path + file
            entity_name = file.replace(".samples", "").replace("EN_RB_ANY_ANY_", "").replace("EN_RB_US_ANY_",
                                                                                             "").replace(
                "EN_RB_US_CFCU_", "")
            file = open(path, "r")
            file = file.readlines()
            temp_values = []
            for line in file:
                temp_values.append(line.replace("\n", ""))

            dicty[entity_name] = temp_values
            entity_names.append(entity_name)
            values.append(temp_values)

    trained_entities_df = pd.DataFrame({'Entitiyname': entity_names,
                                        'values': values, })

    # filename = 'data/cleaned/trained_entities_dict'
    # outfile = open(filename,'wb')
    # pickle.dump(a, outfile)

    trained_entities_df.to_csv('trained_entities.csv')
