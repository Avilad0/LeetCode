from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)

        nearestRightIndex = 0
        while nearestRightIndex<n and startPos>fruits[nearestRightIndex][0]:
            nearestRightIndex+=1
        
        
        # straight right
        currFruits = 0
        currRight = nearestRightIndex
        while currRight<n and fruits[currRight][0]<=startPos+k:
            currFruits+=fruits[currRight][1]
            currRight+=1

        maxFruits = currFruits

        # left and then right majority of Time
        currRight-=1
        nextLeft = nearestRightIndex-1
        while nextLeft>=0 and currRight>=nearestRightIndex:
            diffToCover = 2*(startPos-fruits[nextLeft][0])
            
            if diffToCover>k:
                break

            while currRight>=nearestRightIndex and fruits[currRight][0]>startPos+k-diffToCover:
                currFruits -= fruits[currRight][1]
                currRight-=1
            
            currFruits+=fruits[nextLeft][1]
            maxFruits=max(currFruits, maxFruits)
            nextLeft-=1        


        
        # straight left
        nearestLeftIndex = nearestRightIndex-1 if nearestRightIndex==n or startPos!=fruits[nearestRightIndex][0] else nearestRightIndex
                
        currFruits = 0
        currLeft = nearestLeftIndex
        while currLeft>=0 and fruits[currLeft][0]>=startPos-k:
            currFruits+=fruits[currLeft][1]
            currLeft-=1

        maxFruits = max(maxFruits, currFruits)

        # right and then left majority of Time
        currLeft+=1
        nextRight = nearestLeftIndex+1
        while nextRight<n and currLeft<=nearestLeftIndex:
            diffToCover = 2*(fruits[nextRight][0]-startPos)
            
            if diffToCover>k:
                break

            while currLeft<=nearestLeftIndex and fruits[currLeft][0]<startPos-k+diffToCover:
                currFruits -= fruits[currLeft][1]
                currLeft+=1
            
            currFruits+=fruits[nextRight][1]
            maxFruits=max(currFruits, maxFruits)
            nextRight+=1        


        return maxFruits
    

print(Solution().maxTotalFruits(fruits = [[4,5],[6,1],[11,4],[16,3]], startPos = 15, k = 7)) #Output: 7
# print(Solution().maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4)) #Output: 9
# print(Solution().maxTotalFruits(fruits = [[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]], startPos = 21, k = 30)) #Output: 71