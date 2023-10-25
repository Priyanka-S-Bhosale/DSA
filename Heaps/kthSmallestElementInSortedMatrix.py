#https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                val = matrix[i][j]
                heapq.heappush(heap, -val)
                if len(heap)>k:
                    heapq.heappop(heap)
        return -heap[0]
        
