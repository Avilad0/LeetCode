from typing import List
import heapq

# Shortest Path Faster Algorithm 
# tc=O(f+ n*k)=O(n*k), sc=O(n+f)
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adjList = [[] for _ in range(n)]
        for s,d,cost in flights:
            adjList[s].append((d, cost))
        
        dist = [ float('inf') for _ in range(n)]
        dist[src]=0
        q = deque([(0,0,src)]) # (cost, stops, airportIndex)

        while q:
            # print(q)
            (cost, stops, curr) = q.popleft()

            if stops==k+1:
                continue

            for d, dCost in adjList[curr]:
                if cost+dCost<dist[d]:
                    dist[d]=cost+dCost
                    q.append((cost +dCost, stops+1, d))
            
        return dist[dst] if dist[dst]!=float('inf') else -1
    

# # Bellman-Ford 
# # tc=O((f+n)*k)=O(f*k), sc=O(n)
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
#         dist = [float('inf') for _ in range(n)]
#         dist[src]=0

#         for _ in range(k+1):
#             newDist = dist[:]
#             for s,d,cost in flights:
#                 newDist[d]=min(newDist[d], dist[s]+cost)
#             dist=newDist
        
#         return dist[dst] if dist[dst]!=float('inf') else -1

# # Djikstra's with stops and dist to prevent adding paths with higher cost for same node with same stops
# # tc=O(f*k*log(f*k)), sc=O(f+ n*k + f*k)
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
#         adjList = [[] for _ in range(n)]
#         for s,d,cost in flights:
#             adjList[s].append((d, cost))
        
#         dist = [ [float('inf')]*(k+2) for _ in range(n)]
#         dist[src][0]=0
#         mh = [(0,0,src)] # (cost, stops, airportIndex)

#         while mh:
#             # print(mh)
#             (cost, stops, curr) = heapq.heappop(mh)
#             if curr==dst:
#                 return cost

#             if stops==k+1 or dist[curr][stops]<cost:
#                 continue

#             for d, dCost in adjList[curr]:
#                 if cost+dCost<dist[d][stops+1]:
#                     dist[d][stops+1]=cost+dCost
#                     heapq.heappush(mh, (cost +dCost, stops+1, d))
            
#         return -1