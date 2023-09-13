# https://leetcode.com/problems/path-with-minimum-effort/

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        distance = [[float ('inf')]*m for _ in range(n)]
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap,[0,0,0])
        dRow = [-1,0,1,0]
        dCol = [0,1,0,-1]

        while heap:
            dis,row,col = heapq.heappop(heap)

            if row == n-1 and col == m-1: 
                return dis

            for i in range(4):
                nrow = dRow[i] + row
                ncol = dCol[i] + col
                
                if(nrow>=0 and ncol >=0 and nrow <n and ncol <m):
                    newEffort = max(abs(heights[row][col] - heights[nrow][ncol]),dis)
                    if(newEffort < distance[nrow][ncol]):
                        distance[nrow][ncol] = newEffort
                        heapq.heappush(heap,[newEffort,nrow,ncol])









