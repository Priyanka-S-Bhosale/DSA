#https://leetcode.com/problems/cheapest-flights-within-k-stops/

def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        
        distance=[float('inf') for i in range(n)]

        distance[src]=0
        queue = deque()

        queue.append((-1,src,0))
        while queue:
            stops,node,dis = queue.popleft()

            if stops >=k: 
                continue

            for v,w in graph[node]:
                if(w+dis < distance[v]):
                    distance[v] = w+dis
                    queue.append((stops+1, v, w+dis))
            
        if distance[dst] == float('inf'):
            return -1
    
        return int(distance[dst])
