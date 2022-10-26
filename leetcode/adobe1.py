#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getNumPairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER l
#  3. INTEGER r
#

def getNumPairs(arr, l, r):
    # Write your code here
    count = 0
    for i in range (len(arr)):
        for j in range (i+1, len(arr)):
            if arr[i]+arr[j] <= r and arr[i]+arr[j] >= l:
                count += 1
    return count
        
if __name__ == '__main__':
    print(getNumPairs([6, 2,3000], 30001, 100000))
