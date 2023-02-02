#!/usr/bin/python3
""" Function that multiplies 2 matrices: """


def matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices.
    
    Args:
        m_a (list): A matrix as a list of lists containing integers or floats.
        m_b (list): A matrix as a list of lists containing integers or floats.

    Returns:
        result (list): A matrix representing the product of m_a and m_b.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(j, (int, float)) for i in m_a for j in i):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(j, (int, float)) for i in m_b for j in i):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b)) \
        for col_b in zip(*m_b)] for row_a in m_a]
    return result