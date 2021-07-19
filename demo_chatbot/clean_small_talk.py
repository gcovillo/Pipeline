"""
function clean_small_talk()
Window-open mon,tue,wed,thur,fri,sat,sun 11:20pm
Window-close-in 1hr
run-after get_intent_datas.py
run-at None
"""

import pandas as pd
import os


def clean_small_talk():
    path = "data/raw/v001/SmallTalk/smalltalk.txt"
    small_talk = open(path, "r")
    small_talk = small_talk.readlines()

    user_response = []
    bot_response = []
    temp_bot_response = []

    for line in small_talk:
        if ("[" in line) and ("]" in line):
            user_response.append(line.replace("[", "").replace("]", "").replace("\n", ""))
        elif line.replace(" ", "") == "\n":
            bot_response.append(list(temp_bot_response))
            temp_bot_response.clear()
        else:
            temp_bot_response.append(line.replace("\n", ""))

    small_talk_df = pd.DataFrame({'input': user_response,
                                  'intent': 'small_talk',
                                  'response_array': bot_response})

    small_talk_df.to_csv('small_talk.csv')
