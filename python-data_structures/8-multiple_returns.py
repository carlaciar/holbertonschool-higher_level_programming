#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0

    if sentence != "":
        length = len(sentence)
        first = sentence[0]

    if sentence == "":
        first = "None"

    multiplereturnstuple = ([length, first])
    return multiplereturnstuple
