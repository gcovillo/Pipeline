"""
CTRL-M clean_faq_files()
Window-open mon,tue,wed,thur,fri,sat,sun 11:40pm
Window-close-in 1hr
run-after clean_small_talk.py
run-at None
"""

import pandas as pd
import os


def clean_faq_files():
    faq_files = []
    folder_path = "home/ubuntu/test/data/raw/v001/faqs/"
    folder = os.listdir(folder_path)
    for file in folder:
        if 'FAQ' in file:
            faq_files.append(file)

    path = "data/raw/v001/faqs/"
    topics = []
    subtopics = []
    questions = []
    faq_ids = []
    temp_questions = []
    answers = []

    for file in faq_files:
        new_path = path + file
        faq = open(new_path, "r")
        faq = faq.readlines()

        topic = ''
        subtopic = ''
        faq_id = ''

        for line in faq:
            if ('#' in line[0]) or (line.replace(" ", "") == "\n") or ('[questions]' in line) or ('prefix' in line):
                continue
            elif 'topic' in line:
                topic = line.replace('topic=', '').replace("\n", "")
            elif 'subtop' in line:
                st = line.replace("\n", "").split("=")
                subtopic = st[1]
            elif 'faq' in line:
                faq_id = line.replace(" ", "").replace("\n", "").replace("[", "").replace("]", "").replace("faq:ID_",
                                                                                                           "")
            elif 'answer' in line:
                answer = line.split("</channel>")
                answer = answer[-1].replace("</segment>:", "")
                for q in temp_questions:
                    topics.append(topic)
                    subtopics.append(subtopic)
                    faq_ids.append(faq_id)
                    questions.append(q)
                    answers.append(answer)

                temp_questions.clear()
            else:
                temp_questions.append(line.replace("Question=", "").replace("\n", ""))

    faqs_df = pd.DataFrame({'input': questions,
                            'intent': 'faq',
                            'subintent': faq_ids,
                            'topic': topics,
                            'subtopics': subtopics,
                            'response_array': answers})

    faqs_df.to_csv('faqs.csv')
