#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:01:02 2021
Rotate string
@author: sindy
"""

import unittest


def isRotated(string1):
    
    # string2 = str(input("Introduce a string: "))    
    length = len(string1)
    # print(length, right)
    temp_right = []
    temp_left = []
    
    for char in string1:
        if char in string1[length - length // 2]:
            pivot = char
            # print(pivot)
            right = string1.index(pivot, length // 2, length)            
            for char in range(right, length):
                temp_right.append(string1[char])
            for char in range(0, right):
                temp_left.append(string1[char])
                
            temporal = temp_right + temp_left 
            print(temporal)
  
    return temporal
            


        
    
        
        
   
# string1 = 'mojica'
# temporal = isRotated(string1)        
       
        
        
    
    
    
# string1 = input("Introduce a string: ")   
# string2 = input("Introduce a string: ")    

# print(temporal)
# isSubstring(temporal)
    

class Test(unittest.TestCase): 
    
    def test_isSubstring(self):
        string1 = ['m','o','j','i', 'c', 'a']
        string2 = ['i', 'c', 'a', 'm', 'o', 'j']
        temporal  = isRotated(string1)
        self.assertEqual(string2, temporal)
    
  


if __name__ == "__main__":
    unittest.main()  