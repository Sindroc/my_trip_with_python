#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:44:19 2021
Implement an algorithm to determine if a 
string has all unique characters. 
What if you can not use additional data structures?
@author: sindy
"""


import string
from collections import Counter

alphabet = string.ascii_lowercase
code = """
swodkdbkfovvobpbywkxkxdsaeovkxngrycksndgyfkcdkxndbexuvoccvoqcypcdyx
ocdkxnsxdronocobdxokbdrowyxdrockxnrkvpcexukcrkddobonfsckqovsocgrycop
bygxkxngbsxuvonvszkxncxoobypmyvnmywwkxndovvdrkdsdccmevzdybgovvdrycoz
kccsyxcbokngrsmriodcebfsfocdkwzonyxdrocovspovoccdrsxqcdrorkxndrkdwym
uondrowkxndrorokbddrkdponkxnyxdrozonocdkvdrocogybnckzzokbwixkwoscyji
wkxnskcusxqypusxqcvyyuyxwigybuciowsqrdikxnnoczksbxydrsxqlocsnobowksx
cbyexndronomkiypdrkdmyvycckvgbomulyexnvocckxnlkbodrovyxokxnvofovckxn
ccdbodmrpkbkgki
"""


def count_char(s):
    filtered = [char for char in s.lower() if char in alphabet]
    print(Counter(filtered))
    counter = Counter(filtered)
    return counter


def is_unique(counter):
    for key, char in counter.items():
        if char == 1:
            True 
            print(f'{key} is unique')
        else:
            False 
        print(f'{key} is not unique')
            
counter = count_char(code)
is_unique(counter)






