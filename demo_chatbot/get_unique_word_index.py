"""
function unique_word_intent_subintent_index()
Window-open mon,tue,wed,thur,fri,sat,sun 1am
Window-close-in 1hr
run-after get_unique_intents.py
run-at 1am
"""

'{"links":[{"id":"get_intent_data.py_8","source":"8","target":"9"},{"id":"clean_small_talk.py_9","source":"9","target":"5"},{"id":"clean_faq_files.py_5","source":"5","target":"1"},{"id":"clean_entity_dict.py_1","source":"1","target":"3"},{"id":"clean_entity_regex.py_3","source":"3","target":"2"},{"id":"clean_trained_entities.py_2","source":"2","target":"7"},{"id":"merge_intents.py_7","source":"7","target":"6"},{"id":"get_unique_intents.py_6","source":"6","target":"4"}],"nodes":[{"id":"8","label":"get_intent_data.py","status":"ColorStatus.Default","description":"Job Type: Service","icon":"app_connection"},{"id":"9","label":"clean_small_talk.py","status":"ColorStatus.Default","description":"Job Type: Service","icon":"app_connection"},{"id":"5","label":"clean_faq_files.py","status":"ColorStatus.Default","description":"Job Type: Service","icon":"app_connection"},{"id":"1","label":"clean_entity_dict.py","status":"ColorStatus.Default","description":"Job Type: Service","icon":"app_connection"},{"id":"3","label":"clean_entity_regex.py","status":"ColorStatus.Default","description":"Job Type: Service","icon":"app_connection"},{"id":"2","label":"clean_trained_entities.py","status":"ColorStatus.Default","description":"Job Type: Service","icon":"app_connection"},{"id":"7","label":"merge_intents.py","status":"ColorStatus.Default","description":"Job Type: Service","icon":"app_connection"},{"id":"6","label":"get_unique_intents.py","status":"ColorStatus.Default","description":"Job Type: Service","icon":"app_connection"},{"id":"4","label":"get_unique_word_index.py","status":"ColorStatus.Default","description":"Job Type: Service","icon":"app_connection"}]}'
'import pandas as pd

def unique_word_intent_subintent_index():
    # read in data
    df = pd.read_csv('merged_intent_data.csv', low_memory = False, dtype={'use_case': 'string', 'intent': 'string',
                                                                          'sentence': 'string', 'answer': 'string'})
    mixed = {}
    words = []
    intents = []
    use_cases = []
    counts = []

    # loop through sentences
    for i, sentence in enumerate(df['sentence']):
            # loop through words
            for word in sentence.split(" "):
                intent = df.at[i, 'intent']
                use_case = df.at[i, 'use_case'] # subintent
                combo = str(word) + "_" + str(intent) + "_" + str(use_case)
                # updates the count in the dict
                if combo in mixed.keys():
                    mixed[combo] += 1
                    # add it to the dictionary if its not there
                else:
                    mixed[combo] = 1

    # separate keys, add to lists
    for key in mixed.keys():
        count = mixed[key]
        keys = key.split("_")
        words.append(keys[0])
        intents.append(keys[1])
        use_cases.append(keys[2])
        counts.append(count)

    # write to dataframe
    unique_df = pd.DataFrame({'word': words,
                              'intent': intents,
                              'use_case': use_cases,
                              'count': counts})

    unique_df.to_csv('unique_word_intent_subintent.csv', index = False)