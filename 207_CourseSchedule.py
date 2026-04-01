from typing import List

# DFS approach (with cycle detection and memoization to not check the same path again), 
# tc: O(V + E), sc: O(V + E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # course -> preReq
        adjList = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])
        
        visited = [False]*numCourses
        coursesTaken = [False]*numCourses

        def dfs(currCourse):
            if coursesTaken[currCourse]:
                return True

            if visited[currCourse]:
                return False
            
            visited[currCourse] = True

            for prereq in adjList[currCourse]:
                if not dfs(prereq):
                    return False

            coursesTaken[currCourse] = True
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True