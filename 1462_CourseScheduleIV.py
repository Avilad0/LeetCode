from typing import List
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        course_to_prereq = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            course_to_prereq[b].append(a)

        ans = []
        for u,v in queries:
            queue = deque(course_to_prereq[v])
            visited = [False]*numCourses
            visited[v] = True
            while queue:
                if queue[0]==u:
                    ans.append(True)
                    break
                if not visited[queue[0]]:
                    queue.extend(course_to_prereq[queue[0]])
                visited[queue[0]]=True
                queue.popleft()
            else:
                ans.append(False)
        return ans
    
print(Solution().checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]])) # Output: [false,true]
print(Solution().checkIfPrerequisite(numCourses = 4, prerequisites = [[2,3],[2,1],[0,3],[0,1]] , queries = [[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]])) # Output: [true,true,true,false,false,false]

'''
Input:
numCourses = 4
prerequisites = [[2,3],[2,1],[0,3],[0,1]]
course_to_prereq = [0:, 1:2 ,2: ,3: 2]
queries = [[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]]
Expected : [true,true,true,false,false,false]

'''