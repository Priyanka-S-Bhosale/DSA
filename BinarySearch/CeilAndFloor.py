#https://www.codingninjas.com/studio/problems/ceiling-in-a-sorted-array_1825401?leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

def ceilingInSortedArray(n, x, arr):
    # Write your code here.
    def ceil(arr, x):
        arr.sort()
        n = len(arr)
        l = 0
        r = n-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]>=x:
                ans = arr[mid]
                r = mid -1
            else:
                l = mid +1
        return ans
    def floor(arr, x):
        arr.sort()
        n = len(arr)
        l = 0
        r = n-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]<=x:
                ans = arr[mid]
                l = mid +1
            else:
                r = mid -1
        return ans
    a = floor(arr,x)
    b = ceil(arr,x)
    return "{} {}".format(a, b)
