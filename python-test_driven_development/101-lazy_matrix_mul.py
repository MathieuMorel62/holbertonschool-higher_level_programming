#!/usr/bin/python3
"""  multiplies 2 matrices by using the module NumPy """


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        return np.dot(m_a, m_b).tolist()
    except ValueError as e:
        raise ValueError("matrices are not aligned")
