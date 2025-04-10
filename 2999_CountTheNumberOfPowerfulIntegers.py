class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def count(end: str):
            if len(end)< len(s):
                return 0
            if len(end) == len(s):
                return 1 if end>s else 0
            
            suffix = end[len(end)-len(s):]
            prefixLen = len(end)-len(s)
            numCounts = 0

            for i in range(prefixLen):
                if limit < int(end[i]):
                    numCounts += (limit + 1) ** (prefixLen - i) #every number starting from and including this number can be upto limit. No calculation required further and return it.
                    return numCounts
            
                numCounts += int(end[i]) * (limit + 1) ** (prefixLen - 1 - i) # every number after this can be upto limit for this number less than end[i]. For equal to end[i], check further.

            if suffix >= s:
                numCounts += 1 # if not any number before suffix is more than limit, we need to check if the suffix is also more than s.

            return numCounts           
            

        return count(str(finish)) - count(str(start-1))