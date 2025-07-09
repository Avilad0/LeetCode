from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        currDuration = 0
        maxFreeDuration = 0
        
        for i in range(n):
            currDuration += endTime[i] - startTime[i] 
            currWindowStart = 0 if i<k else startTime[i-k]
            nextEventStart = eventTime if i==n-1 else startTime[i+1]

            maxFreeDuration = max(maxFreeDuration, nextEventStart - currWindowStart - currDuration)
            if i>=k:
                currDuration -= (endTime[i-k] - startTime[i-k])

        return maxFreeDuration



print(Solution().maxFreeTime(eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]))
print(Solution().maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]))