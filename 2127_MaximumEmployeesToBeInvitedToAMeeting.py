from typing import List
from collections import deque

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)

        indegree = [0]*n
        for person in range(n):
            indegree[favorite[person]]+=1


        queue = deque([person for person in range(n) if indegree[person]==0])

        depth = [1]*n

        while queue:
            currPerson = queue.popleft()
            nextPerson = favorite[currPerson]

            depth[nextPerson] = max(depth[nextPerson], depth[currPerson]+1)

            indegree[nextPerson] -= 1

            if indegree[nextPerson] == 0:   #only add non-cycle persons
                queue.append(nextPerson)
        
        longestCycle = 0
        twoPersonCycleTotal = 0

        for person in range(n):
            if indegree[person]==0:
                continue

            cycleLength = 0
            curr = person
            while indegree[curr]!=0:
                indegree[curr] = 0
                cycleLength+=1
                curr = favorite[curr]
            
            if cycleLength == 2:
                twoPersonCycleTotal+=depth[person] + depth[favorite[person]]
            else:
                longestCycle = max(longestCycle, cycleLength)

        return max(longestCycle, twoPersonCycleTotal)