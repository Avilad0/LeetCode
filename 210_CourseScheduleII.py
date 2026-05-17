from typing import List
from collections import deque

# tc = O(V+E), tc = O(V+E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0]*numCourses
        adjList = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            adjList[p].append(c)
            indegree[c]+=1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        order = []
        while q:
            course = q.popleft()
            order.append(course)

            for nxt in adjList[course]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    q.append(nxt)
        
        return order if len(order)==numCourses else []
                    

