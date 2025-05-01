from typing import List
import bisect

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        m,n = len(workers), len(tasks)

        def isPossible(mid:int)-> bool:
            currPills = pills
            orderedSetWorkers = workers[-mid:]

            for i in range(mid-1,-1,-1):
                if tasks[i]<=orderedSetWorkers[-1]:
                    orderedSetWorkers.pop()
                else:
                    if currPills==0 :
                        return False
                    
                    rep = bisect.bisect_left(orderedSetWorkers, tasks[i]-strength)
                    if rep == len(orderedSetWorkers):
                        return False
                    
                    currPills-=1
                    orderedSetWorkers.pop(rep)
            
            return True
        
        low, high = 1, min(m, n)
        ans = 0

        while low<=high:
            mid = (low+high)//2
            if isPossible(mid):
                ans = mid
                low = mid+1
            else :
                high = mid-1
        
        return ans