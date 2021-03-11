#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:36:51 2021
Design an algorithm and write code to remove the 
duplicate characters in a string without using any 
additional buffer. NOTE: One or two additional 
variables are fine. An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.
@author: sindy
"""

from collections import Counter

def count_letters(s):
    single = []
    filtered = [char for char in s.lower() if char in alphabet]
    counter = Counter(filtered)
    # print(counter)
    value = counter.values() 
    key = counter.values()
    for key, value in counter.items():
        if value != 1:
           del key
        else:
           single.append(key)
    return single
    
        

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
alphabet = "abcdefghijklmnopqrstuvwxyz"
unique = count_letters(code)
print(unique)