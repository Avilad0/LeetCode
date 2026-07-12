from typing import List

# Prims Optimal (without heap)
# tc=O(n^2), sc=O(n)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        dist = {}
        for i in range(1,len(points)):
            dist[i]=abs(points[i][0]-points[0][0]) + abs(points[i][1]-points[0][1])

        while dist:
            minI = -1
            for i in dist.keys():
                if minI==-1 or dist[i]<dist[minI]:
                    minI=i
            
            cost+=dist[minI]
            dist.pop(minI)
            for i in dist.keys():
                dist[i]=min(dist[i], abs(points[i][0]-points[minI][0]) + abs(points[i][1]-points[minI][1]))

        return cost