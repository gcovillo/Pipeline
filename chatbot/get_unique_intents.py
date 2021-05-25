"""
CTRL-M get_unique_intents()
Window-open mon,tue,wed,thur,fri,sat,sun 1am
Window-close-in 1hr
run-after clean_trained_entities.py
"""
import pandas as pd
import os


def get_unique_intents():
    df = pd.read_csv('../data/cleaned/IntentData.csv')
    words = [] 
    word_dict = [] 


    for i, sentence in enumerate(df['sentence']):
        dont_do = 0
        temp_dict = {}
        for word in sentence.split(" "):
            use_case = df.at[i, 'use_case']
            intent = df.at[i, 'intent']
            pairing = {use_case:intent}
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