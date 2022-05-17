"""
function clean_trained_entities()
window_open mon,tue,wed,thur,fri
window_open_time 12:50am
window_close_in 1hr
dont_run_time 4pm
dont_run_day sun
group_name chatbot
owner gillian covillo
pipeline c3p0
run_after clean_entity_regex.py max_age 2 days
run_at 6pm
"""

import pandas as pd
import os


def clean_trained_entities():
    dicty = {}

    entity_names = []
    values = []
    folder_path = "data/raw/v001/Entity Data/"
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
