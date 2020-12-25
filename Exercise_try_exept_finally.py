#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:56:10 2020
# below is the AI 1.0 code, which works but cannot handle invalid input
# if the user input something other than an integer at first, the program will break due to a ValueError,
# caused by calling int() function on an non-integer input result
#
# Your task is to use the try-except-else-finally workflow to improve the existing code
# which can detect an invalid input in the beginning, and prints our an error message: 'Please input integers only.'
# then proceed to ask the user 'Do you want to play again? (y/N):' like the original function does
@author: sindy
"""


def interact():
    while True:  # keep looping until user reach break statement
        try:            
            user_input = int(input('Please input an integer:'))     # turn the user input into an integer
#            break   # break the while loop to quit
        except ValueError:
            print(f'Please enter integers only') 
        else: 
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))     # print out the message '{user_input} is {even/odd}.'
        finally:
            user_input = input('Do you want to play again? (y/N):')
            if user_input != 'y':   # quit if the user didn't input `y`
                print('Goodbye.')
                break

#            print('Goodbye.')      
         
SETUP = 'counter = 0'

LOOP_IF = """
counter += 1
"""

LOOP_EXCEPT = """
try:
    counter += 1
except:
    pass
"""


if __name__ == '__main__':
    import timeit
    if_time = timeit.Timer(LOOP_IF, setup=SETUP)
    except_time = timeit.Timer(LOOP_EXCEPT, setup=SETUP)
    print('using if statement: {}'.format(min(if_time.repeat(number=10 ** 7))))
    print('using exception: {}'.format(min(except_time.repeat(number=10 ** 7))))

                                         
interact()           





