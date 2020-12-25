#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:10:39 2020
# - define a UncountableError that takes in wrong_value as the only argument
# - the UncountableError should inherit ValueError
# - the UncountableError should indicate an error message like this:
#    'Invalid value for n, WRONG_VALUE. n must be greater than 0.'
#    where WRONG_VALUE should be replaced by the given value in the argument
@author: sindy
"""


# define your UncountableError here:

class UncountableError(ValueError):
    def __init__(self, wrong_value):
        super().__init__(f'Invalid value for n, {wrong_value}. n must be greater than 0')
        
# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way


def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)
        
wrong_value =  int(input("Introduce the value of n: "))
count_from_zero_to_n(wrong_value)

