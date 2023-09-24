# https://www.codingninjas.com/studio/problems/smallest-divisor-with-the-given-limit_1755882?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=1

from os import *
from sys import *
from collections import *
from math import *
import math


def smallestDivisor(arr: [int], limit: int) -> int:
    # Write your code here.
    def divisorSum(arr, divisor):
        sumOfDivisions = 0
        for i in range(len(arr)):
            sumOfDivisions += math.ceil(arr[i]/divisor)
        return sumOfDivisions
        
    
    if len(arr) > limit:
        return -1
    l = 1
    r = max(arr)

    while l<=r:
        mid = (l+r)//2
        val = divisorSum(arr, mid)

        if val <= limit:
            r = mid -1
        else:
            l = mid+1
    return l

    
