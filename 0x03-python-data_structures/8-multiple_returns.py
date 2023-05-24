#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    if sentence == "":
        first = None
    else:
        first = sentence[0]
    lenght = len(sentence)
    tuples = (lenght, first)
    return (tuples)
