#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        target_tuple = (len(sentence), None)
        return target_tuple
    else:
        target_tuple = (len(sentence), sentence[0])
        return target_tuple


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
