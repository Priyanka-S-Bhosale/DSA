#https://www.codingninjas.com/studio/problems/capacity-to-ship-packages-within-d-days_1229379?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=1

from os import *
from sys import *
from collections import *
from math import *

def leastWeightCapacity(weights, d):
    # Write your code here.
    def findDays(capacity, arr):
        load = 0
        noOfDays = 1

        for i in range(len(arr)):
            
            if load + arr[i] > capacity:
                noOfDays +=1
                load = arr[i]
            else:
                load += arr[i]
        return noOfDays

    l = max(weights)
    r = sum(weights)

    while l<=r:
        mid = (l+r)//2

        days = findDays(mid,weights)
        if days<= d:
            r = mid -1
        else:
            l = mid +1
        
    return l

