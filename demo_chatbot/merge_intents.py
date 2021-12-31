# noinspection PyInterpreter
"""
function merge_intents()
Window-open mon,tue,wed,thur,fri,sat,sun 12:30am
Window-close-in 1hr
run-after clean_trained_entities.py
"""

import pandas as pd
import numpy as np

def merge_intents():
    NaN = np.nan
    intent_data = pd.read_csv("intent_data.csv")
    faq_data = pd.read_csv("faqs.csv")
    smalltalk_data = pd.read_csv("small_talk.csv")
    
    # drop unnecessary columns/merge data
    # use_case | intent | sentence | answer

    # create answer column = blank
    intent_data['answer'] = NaN

    # create use_case = subintent, sentence = input, answer = response_array
    # delete/ignore subintent columns, input column, response_array, topic, subtopic
    faq_data = faq_data.rename(columns = {'subintent' : 'use_case', 'input' : 'sentence', 'response_array' : 'answer'})
    faq_data = faq_data.drop(['topic', 'subtopics'], axis=1)

    # create sentence = input, use_case = blank, answer = response_array
    # delete/ignore input, response_array
    smalltalk_data = smalltalk_data.rename(columns = {'input' : 'sentence', 'response_array' : 'answer'})
    smalltalk_data['use_case'] = NaN

    # merge into one dataframe
    frames = [intent_data, faq_data, smalltalk_data]
    merged = pd.concat(frames).drop(['Unnamed: 0'], axis = 1)
    merged.to_csv('merged_intent_data.csv', index = False)