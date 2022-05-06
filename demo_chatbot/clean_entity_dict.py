"""
function clean_entity_dict()
Window-open mon,tue,wed,thur,fri,sat,sun 12:10am
Window-close-in 1hr
run-after clean_faq_files.py
run-at none
"""
import pandas as pd
import os



def clean_entity_dict():
    dicts = []
    folder_path = "data/raw/v001/Entity Data/"
    folder = os.listdir(folder_path)
    for file in folder:
        if 'dict' in file:
            dicts.append(file)

    true_entities = []
    accepted_entities = []
    entities = []

    for file in dicts:
        entity_name = file.replace("_dict", "").replace("EN_RB_ANY_ANY_", "").replace("EN_RB_US_ANY_", "").replace(
            "EN_RB_US_CFCU_", "")
        path = folder_path + file
        entity_file = open(path, "r")
        entity_file = entity_file.readlines()
        for line in entity_file:
            line = line.replace("\n", "")
            r = line.split("=")
            true_entities.append(r[0])
            if entity_name in entities:
                ind = entities.index(entity_name)
                temp = list(r[1].split(","))
                for item in temp:
                    accepted_entities[ind].append(item)
            else:
                accepted_entities.append((list(r[1].split(","))))
                entities.append(entity_name)

    entity_df = pd.DataFrame({'Entityname': entities,
                              'values': accepted_entities})

    entity_df.to_csv('entity_dict.csv')
