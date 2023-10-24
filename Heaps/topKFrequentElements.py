# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from collections import defaultdict
#hashmap of frequencies
#heap array
#heapify it
#for key,val in hashmap. heppush(val,key)
#if len(heap) >k, heappop
#return pair[1] for pair in heap as we want keys
# TC: O(nlogK) k for hepa elements , n for nums 
#O(n+k) n : hashmap, k heap elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] +=1
        heap = []
        heapq.heapify(heap)
        for key,val in hashmap.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        return [pair[1] for pair in heap]
