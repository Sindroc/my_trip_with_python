#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:04:10 2021
Write a method to decide if two 
strings are anagrams or not.
@author: sindy
"""

def anagram():
    word1 = input('first word: ')
    word2 = input('second word: ')
    
    if sorted(word1) == sorted(word2):
        print("This is an anagram")
    else:
        print("This is not an anagram")
          
anagram()