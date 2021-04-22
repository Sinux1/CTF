#!/bin/python3
from ast import literal_eval

from MaxSubArray import maxSubArraySum

m = "[[6, -5, -7, 4, -4], [-9, 3, -6, 5, 2], [-10, 4, 7, -6, 3], [-8, 9, -3, 3, -7]]"


def findMaxSum(matrice):
    maxSum = 0
    ncol = len(matrice)
    nrow = len(matrice[0])

    for left in range(ncol):
        temp = []
        for n in range(ncol):
            temp.append(0)
        for right in range(left, ncol):
            for i in range(nrow):
                print(i)
                print("Left {} : Right {}\n NRows {} : NCol {}".format(left, right, nrow, ncol))
                temp[i] += matrice[i][right]

            sum = maxSubArraySum(temp, len(temp))
            if sum > maxSum:
                maxSum = sum
    return maxSum


m = "[[6, -5, -7, 4, -4], [-9, 3, -6, 5, 2], [-10, 4, 7, -6, 3], [-8, 9, -3, 3, -7]]"
mat = literal_eval(m)
findMaxSum(mat)
