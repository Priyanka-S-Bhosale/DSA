#https://www.codingninjas.com/studio/problems/kth-missing-element_893215?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=1
from typing import *

def missingK(arr: List[int], n: int, k: int) -> int:
    # Write your code here.
    l = 0
    n = len(arr)
    r = n - 1

    while l<=r:
        mid = (l+r)//2
        missing = arr[mid] - (mid+1)
        if missing < k:
            l = mid +1
        else:
            r = mid -1
    #arr[r] + more
    #arr[r] + k -(arr[r] - r - 1)
    #arr[r] + k - arr[r] +r +1
    # k + r + 1
    # or k + l
    return k + r + 1
