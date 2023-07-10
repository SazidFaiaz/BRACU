import numpy as np
from numpy import *

# def creat_matrix():
#     matrix = np.zeros((2,2) , dtype=int)
#     for i in range(2):
#         for j in range(2):
#             matrix[i][j] = int(input("enter value:" ))
#
#     return matrix
#Row wise:
# def print_row(matrix):
#     row , col = matrix.shape
#     print(matrix.shape)
#     for i in range(row):
#         for j in range(col):
#             print(matrix[i][j] , end=" ")
#
#         print()
#     return None
# matrix = array([[1,2],[3,4],[4,5]])
# print(print_row(matrix))

#Colum wise:

def print_col(m):
    row , col = m.shape
    for i in range(col):
        for j in range(row):
            print(m[j][i] , end=" ")

        print()
    return m
m = array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(print_col(m))