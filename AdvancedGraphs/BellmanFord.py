#https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

from collections import defaultdict
class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
  
        
        dist = [100000000] * V # Here fallback was expected to be 10 ^ 8 insted of Inf 
        dist[S] = 0
        for count in range(V - 1): # important to move V - 1 Times, count is not used anywhere 
            for s,d,w in edges:
                if dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        for s,d,w in edges:
            if dist[s] + w < dist[d]:
                return [-1]
        return dist        
        
    
