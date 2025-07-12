from typing import List
from functools import cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        return self.possibilities(n,firstPlayer, secondPlayer)
    
    @cache
    def possibilities(self, n: int, firstPlayer: int, secondPlayer: int):
        newN = (n+1)//2
        if n==2 or firstPlayer == n-secondPlayer+1:
            return [1,1]
        
        firstPlayerBit, secondPlayerBit = firstPlayer-1, secondPlayer-1
        minSteps, maxSteps = newN, 1
        middleElement = ('' if n%2==0 else '1')
        firstHalfPos = (1<<(n//2))
        for i in range(firstHalfPos):
            currBin = bin(i)[2:].zfill(n // 2)
            flipped = ''.join('1' if b == '0' else '0' for b in currBin[::-1])
            currPos = int(currBin + middleElement + flipped, base=2)
            if ((currPos>>firstPlayerBit)&1) and ((currPos>>secondPlayerBit)&1):

                newFirstPlayer, newSecondPlayer = -1, -1
                j, setBits =0,0
                while newFirstPlayer==-1 or newSecondPlayer==-1:
                    setBits += ((currPos>>j)&1)
                    if j==firstPlayerBit:
                        newFirstPlayer = setBits
                    if j==secondPlayerBit:
                        newSecondPlayer = setBits
                    j+=1
                
                nextPossibilites = self.possibilities(newN, newFirstPlayer, newSecondPlayer)
                minSteps, maxSteps = min(minSteps, 1+nextPossibilites[0]), max(maxSteps, 1+nextPossibilites[1])

        return [minSteps,maxSteps]

    

print(Solution().earliestAndLatest(n = 11, firstPlayer = 2, secondPlayer = 4 ))   # Output: [3,4]
print(Solution().earliestAndLatest(n = 5, firstPlayer = 1, secondPlayer = 5))   # Output: [1,1]
print(Solution().earliestAndLatest(n = 5, firstPlayer =2, secondPlayer = 5))   # Output: [2,2]
print(Solution().earliestAndLatest(n = 10, firstPlayer = 1, secondPlayer = 8 ))   # Output: [2,3]