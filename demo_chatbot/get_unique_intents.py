import pandas as pd
import os
from mario import set_schedule

@set_schedule(function = "get_unique_intents()",
              runAfter = 'merge_intents.py', maxAge = '1hr',
              windowOpen = "mon,tue,wed,thur,fri,sat,sun",
              windowOpenTime = '12:30am',
              windowCloseIn = '1hr')
def get_unique_intents():
    df = pd.read_csv('merged_intent_data.csv', low_memory = False, dtype={'use_case': 'string', 'intent': 'string',
                                                                          'sentence': 'string', 'answer': 'string'})
    words = []
    word_dict = []

    for i, sentence in enumerate(df['sentence']):
        for word in sentence.split(" "):
            use_case = df.at[i, 'use_case']
            intent = df.at[i, 'intent']
            pairing = {use_case: intent}
            if word not in words:
                words.append(word)
                word_dict.append([pairing])
            else:
                ind = words.index(word)
                need_to_update = word_dict[ind]
                if pairing not in need_to_update:
                    word_dict[ind].append(pairing)

    unique_intents = pd.DataFrame({'Unique Word': words,
                                   'Use_Case | Intent': word_dict})

    unique_intents.to_csv('unique_intents.csv')