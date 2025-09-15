#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = len([i for i in arr if i>0])
    neg = len([i for i in arr if i<0])
    ze = len([i for i in arr if i==0])
    len_arr = len(arr)

    r_pos = round((pos/len_arr), 6)
    r_neg = round((neg/len_arr), 6)
    r_ze = round((ze/len_arr), 6)
    
    print(f"{r_pos}\n{r_neg}\n{r_ze}")
    
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
