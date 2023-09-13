#https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/0

import heapq
from collections import defaultdict
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        graph = defaultdict(list)
        for u in range(V):
            for v, weight in adj[u]:
                graph[u].append((v, weight))
        
        distance = [float('inf')] * V
        heap = []
        heapq.heapify(heap)
        distance[S] = 0
        heapq.heappush(heap, [0, S])
        
        while heap:
            dis, node = heapq.heappop(heap)
            for v, w in graph[node]:
                if dis + w < distance[v]:
                    distance[v] = dis + w
                    heapq.heappush(heap, [dis + w, v])
        
        return distance
        
