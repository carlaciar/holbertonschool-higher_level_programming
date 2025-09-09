#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]

    if sentence == None:
        first = None

    multiplereturnstuple = ([length, first])
    return multiplereturnstuple
