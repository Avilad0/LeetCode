from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        maxFree = startTime[0]

        maxAvailableFreeTime = 0
        for i in range(n):
            prevEndTime = 0 if i==0 else endTime[i-1]
            nextStartTime = eventTime if i==n-1 else startTime[i+1]
            currEventTime = endTime[i]-startTime[i]

            if currEventTime <= maxAvailableFreeTime:
                maxFree = max(maxFree, nextStartTime-prevEndTime)
            else:
                maxFree = max(maxFree, nextStartTime-prevEndTime - currEventTime)

            maxAvailableFreeTime = max(maxAvailableFreeTime, startTime[i]-prevEndTime)
        
        maxAvailableFreeTime = 0
        for i in range(n-1,-1,-1):
            prevEndTime = 0 if i==0 else endTime[i-1]
            nextStartTime = eventTime if i==n-1 else startTime[i+1]
            currEventTime = endTime[i]-startTime[i]

            if currEventTime <= maxAvailableFreeTime:
                maxFree = max(maxFree, nextStartTime-prevEndTime)
            else:
                maxFree = max(maxFree, nextStartTime-prevEndTime - currEventTime)

            maxAvailableFreeTime = max(maxAvailableFreeTime, nextStartTime - endTime[i])

        
        return maxFree


print(Solution().maxFreeTime(eventTime = 5, startTime = [1,3], endTime = [2,5]))    # Output: 2
print(Solution().maxFreeTime(eventTime = 41, startTime = [17,24], endTime = [19,25]))   # Output: 24