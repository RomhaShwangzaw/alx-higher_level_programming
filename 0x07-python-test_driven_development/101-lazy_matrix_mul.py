#!/usr/bin/python3
''' THIS IS A MODULE THAT MULTIPLIES TWO MATRICES USING THE NUMPY MODULE '''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    ''' Multiplies two matrices using the NumPy module and
        returns the resulting matrix '''

    return np.matmul(m_a, m_b)
