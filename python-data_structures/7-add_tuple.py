#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    first_elem = 0
    second_elem = 0

    if len(tuple_a) > 0:
        first_elem = first_elem + tuple_a[0]
    else:
        first_elem = first_elem + 0

    if len(tuple_b) > 0:
        first_elem = first_elem + tuple_b[0]
    else:
        first_elem = first_elem + 0

    if len(tuple_a) > 1:
        second_elem = second_elem + tuple_a[1]
    else:
        second_elem = second_elem + 0

    if len(tuple_b) > 1:
        second_elem = second_elem + tuple_b[1]
    else:
        second_elem = second_elem + 0

    return (first_elem, second_elem)
