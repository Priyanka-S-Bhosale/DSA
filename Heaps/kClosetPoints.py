#https://leetcode.com/problems/k-closest-points-to-origin/

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for x,y in points:
            distance = -(x**2 + y**2)
            heapq.heappush(heap, [distance,x,y])
            print(heap)

            if len(heap) >k:
                heapq.heappop(heap)
        return [[x,y] for distance,x,y in heap]
