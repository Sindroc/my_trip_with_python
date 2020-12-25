#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:22:17 2020

@author: sindy
"""

import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

#print(winner_player)
    # The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
init_match = players[0]
for values in players: 
    numbers_matched = values['numbers'].intersection(lottery_numbers)
    winner = len(numbers_matched) 
    if (winner > len(init_match['numbers'].intersection(lottery_numbers))):
        init_match = values
#            winning = 100**len(numbers_matched)    
winning = 100**len(numbers_matched)
print(f"{init_match['name']} won {winning}")


    

