"""
CTRL-M get_intent_data()
Window-open mon,tue,wed,thur,fri,sat,sun 11pm
Window-close-in 1hr
run-at none
"""

import pandas as pd
import os


def get_intent_data():
    true_path = (os.path.abspath(os.curdir))
    os.chdir('..')
    os.chdir('..')
    folder_path = "test/data/raw/v001/Intent Data"
    folder = os.listdir(folder_path)

    intents = []
    intents2 = []
    entities = []
    requests = []
    use_cases = []
    use_cases2 = []

    for file in folder:
        use_case = file.replace("_primaryClassifier.train.csv", "").replace("EN_RB_ANY_ANY_", "").replace(
            "EN_RB_US_ANY_", "").replace("EN_RB_US_CFCU_", "")
        if file == ".DS_Store" or file == ".ipynb_checkpoints":
            continue
        path = folder_path + file
        file = open(path, "r")
        file = file.readlines()

        intent = ''
        for line in file:
            if ("#" in line) or ("modifier" in line) or ("Utterances" in line) or (line.replace(" ", "") == "\n"):
                continue
            elif 'intent' in line:
                intent = line.replace('intent=', "").replace("\n", "")
            elif 'entities=' in line:
                entity = line.replace("entities=", "").replace("\n", "").split(",")
                for item in entity:
                    entities.append(item)
                    intents2.append(intent)
                    use_cases2.append(use_case)
            else:
                request = line.replace("\n", "")
                requests.append(request)
                intents.append(intent)
                use_cases.append(use_case)

    intent_df = pd.DataFrame({'use_case': use_cases,
                              'intent': intents,
                              'sentence': requests})

    intent_entities = pd.DataFrame({'use_case': use_cases2,
                                    'intent': intents2,
                                    'entities': entities})

    intent_df.to_csv(true_path + 'IntentData.csv')
    intent_entities.to_csv(true_path + 'IntentEntities.csv')

    # return intent_df, intent_entities

