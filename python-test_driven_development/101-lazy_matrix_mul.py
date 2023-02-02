#!/usr/bin/python3
"""  multiplies 2 matrices by using the module NumPy """


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ multiplies 2 matrices """
    try:
        return repr(np.matmul(m_a, m_b))
    except ValueError as e:
        raise ValueError("Error: Scalar operands are not allowed, use '*' instead")
