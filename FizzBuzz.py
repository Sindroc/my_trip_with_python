#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:15:08 2020

@author: sindy
"""

#for element in range(1, 101):
#  if element % 3 == 0 and element % 5 == 0:
#    print(f'{element}, FizzBuzz' )
#    continue
#  if element % 3 == 0:
#    print(f'{element}, Fizz')
#    continue
#  if element % 5 == 0:
#    print(f'{element}, Buzz')
#    continue
#  else:
#    print(f'{element}')

for n in range(1,101):
  if n % 3 == 0 and n % 5==0:
    print("FizzBuzz") 
    continue
  if n % 3 == 0:
      print("Fizz")
      continue
  if n % 5 ==0:
      print("Buzz")
      continue
  else:
       print(n)