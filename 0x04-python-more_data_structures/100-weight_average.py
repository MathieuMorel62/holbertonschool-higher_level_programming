#!/usr/bin/python3


def weight_average(my_list=[]):

    sum_of_products = 0
    sum_of_weights = 0

    if not my_list:
        return 0
    for score, weight in my_list:
        sum_of_products += score * weight
        sum_of_weights += weight
    return sum_of_products / sum_of_weights
