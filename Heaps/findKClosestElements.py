#https://leetcode.com/problems/find-k-closest-elements/

import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        heapq.heapify(heap)

        for i in arr:
            dist = abs(i-x)
            heapq.heappush(heap, (-dist,-i))
            if len(heap) >k:
                heapq.heappop(heap)
        
        return sorted([-pair[1] for pair in heap])
