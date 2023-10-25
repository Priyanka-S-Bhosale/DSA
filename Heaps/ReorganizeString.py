#https://leetcode.com/problems/reorganize-string/

from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = defaultdict(int)
        for i in s:
            hashmap[i] += 1
        heap = []
        heapq.heapify(heap)
        for key, val in hashmap.items():
            heapq.heappush(heap, [-val,key])
        res = []
        while len(heap) >=2:
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)

            res.append(char1)
            res.append(char2)

            if freq1 + 1 < 0:
                heapq.heappush(heap, [freq1 + 1, char1])
            if freq2 + 1 < 0:
                heapq.heappush(heap, [freq2 + 1, char2])
        if heap:
            freq, char = heapq.heappop(heap)
            if -freq > 1:
                return ""
            res.append(char)
            
        return "".join(res)
