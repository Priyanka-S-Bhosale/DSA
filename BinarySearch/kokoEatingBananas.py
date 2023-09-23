#https://www.codingninjas.com/studio/problems/minimum-rate-to-eat-bananas_7449064?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=1

import math
def minimumRateToEatBananas(piles: [int], h: int) -> int:
    # Write Your Code Here.
    def check(k):
        hour = 0
        for i in piles:
            hour = hour + math.ceil(i/k)
            
        return hour <= h
        
        
    left = 1
    right = max(piles)
    
    while left <= right:
        mid = (left+right)//2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left
