#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:46:20 2021
Write an algorithm such that if an element
in a MXN matrix is zero, its entire row and
column are zero.
@author: sindy
"""
import unittest

def zero_matrix(original_mat):
    m = len(original_mat)
    n = len(original_mat[0])
    rows = []
    cols = []
    
    for i in range(m):
        for j in range(n):
            if original_mat[i][j] == 0:
                rows.append(i)
                cols.append(j)   
                # print(original_mat)
    for row in rows:
        zero_row(original_mat, row)        

    for col in cols:
        zero_col(original_mat, col)      
                
    return original_mat
  
    
def zero_row(original_mat, row):
    m = len(original_mat)    
    for i in range(0,m):
        original_mat[row][i] = 0
        
def zero_col(original_mat, col):     
    n = len(original_mat[0])
    for i in range(0,n):
        original_mat[i][col] = 0
    
    
A = [[1,2,3], [4,0,6], [7,8,9]]    
original = zero_matrix(A)
print(original)


class Test(unittest.TestCase):
    
    def test_zero(self):
        matrix1 =  [[1,2,3], 
                    [4,0,6], 
                    [7,8,9]] 
        
        matrix2 =  [[1,0,3], 
                    [0,0,0], 
                    [7,0,9]]  
        zero_matrix(matrix1)
        self.assertEqual(matrix1, matrix2)



            
if __name__ == "__main__":
    unittest.main()        
    







