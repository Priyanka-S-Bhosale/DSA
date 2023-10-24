#https://leetcode.com/problems/top-k-frequent-words/

from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = defaultdict(int)

        for i in words:
            hashmap[i] += 1
        
        heap = []
        heapq.heapify(heap)

        for key,val in hashmap.items():
            heapq.heappush(heap, [-val, key])
        res = [] 
        for _ in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)
                
        return res
