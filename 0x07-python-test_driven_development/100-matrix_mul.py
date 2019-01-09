#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for i, j in zip(m_a, m_b):
        if not isinstance(i, list):
            raise TypeError('m_a must be a list of lists')
        elif not isinstance(j, list):
            raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    elif len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for i, j in zip(m_a, m_b):
        for k in i:
            if not isinstance(k, int) and not isinstance(k, float):
                raise TypeError('m_a should contain only integers or floats')
        for n in j:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError('m_b should contain only integers or floats')
    for i, j in zip(m_a, m_b):
        if len(i) != len(m_a[0]):
            raise TypeError('each row of m_a must should be of the same size')
        elif len(j) != len(m_b[0]):
            raise TypeError('each row of m_b must should be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    prod_m = [[m_a[i][j] * m_b[j][i] for j in range(len(m_b))] for i in range(len(m_b))]
    return [sum(i) for i in prod_m]
