#!/usr/bin/python3
"""Defines a matrix multiplication function using numpy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices."""
    return numpy.matmul(m_a, m_b)


if __name__ == "__main__":
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
