#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    weighted_score = 0
    total_weight = 0
    for intuple in my_list:
        weighted_score += intuple[0] * intuple[1]
        total_weight += intuple[1]
    average = weighted_score / total_weight
    return average
