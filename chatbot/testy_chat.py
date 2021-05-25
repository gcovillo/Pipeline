"""
CTRL-M test()
Window-open mon,tue,wed,thur,fri,sat,sun 1am
Window-close-in 1hr
run-after get_unique_intents.py
group_name chatbots
run-at 1am
"""

def test():
    print("This is fake")