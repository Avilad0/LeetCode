##not done

from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 1 or n==0:
            return len(tasks)
        
        
        countMap={}
        maxx=1
        for t in tasks:
            if t in countMap:
                countMap[t] +=1
                maxx = max(maxx, countMap[t])
            else:
                countMap[t] = 1
        
        print(countMap)

        queue = [[] for i in range(maxx+1)]
        
        for c in countMap.keys():
            queue[countMap[c]].append(c)

        print(queue)

        r=0
        idleC = 0
        i= maxx
        while i!=0:
            lc = len(queue[i])
            lp = len(queue[i-1])

            r+= lc + idleC
            idleC = max(n - lc - lp + 1, 0)

            queue[i-1].extend(queue[i])
            i-=1
            print(r)

        return r
    
print(Solution().leastInterval(["A","A","A","B","B","B"],2))