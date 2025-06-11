class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        validChars = ["0","1","2","3","4"]

        def getStatus(count1, count2) -> int:
            return ((count1&1)<<1) | (count2&1)

        maxDiff = float('-inf')
        for num1 in validChars:
            for num2 in validChars:
                if num1==num2:
                    continue

                best = [float('inf')]*4
                count1, count2 = 0, 0
                prev1, prev2 = 0, 0
                left = -1
                for right in range(n):
                    count1 += (s[right]==num1)
                    count2 += (s[right]==num2)
                    while right-left >=k and count2-prev2>=2:
                        leftStatus = getStatus(prev1, prev2)

                        best[leftStatus] = min(best[leftStatus], prev1-prev2)
                        left+=1
                        prev1 += (s[left]==num1)
                        prev2 += (s[left]==num2)
                    
                    rightStatus = getStatus(count1, count2)
                    if best[rightStatus ^ 0b10] != float('inf'):
                        maxDiff = max(maxDiff, count1-count2 - best[rightStatus ^ 0b10])

        return maxDiff