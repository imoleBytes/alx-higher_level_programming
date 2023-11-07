#!/usr/bin/python3

"""pascal triangle """


def factorial(n):
    """compute the factorial"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


def get_list_of_n(num):
    """returns the pascal values for a number"""
    ls = []
    for i in range(num):
        v = factorial(num) // (factorial(i) * factorial(num - i))
        ls.append(v)
    ls.append(1)
    return ls


def pascal_triangle(n):
    """lists of all the pascal values up till number"""
    final_list = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        final_list.append(get_list_of_n(i))
    return final_list
