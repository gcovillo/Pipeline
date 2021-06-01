"""
function unique_word_intent_subintent_index()
Window-open mon,tue,wed,thur,fri,sat,sun 1am
Window-close-in 1hr
run-after get_unique_intents.py
run-at 1am
"""
import pandas as pd

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