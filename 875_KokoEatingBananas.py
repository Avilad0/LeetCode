from typing import List

# tc=O(n*log(m)) [n=len(piles), m=max(piles)], sc=O(1) - binary search k 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        mink, maxk = 1, max(piles)        

        ans = -1
        while mink<=maxk:
            midk = (mink+maxk)//2

            currh = 0
            for pile in piles:
                currh+= ((pile + midk-1)//midk)  #add midk-1 to pile to get ceil value
            
            if currh<=h:
                ans = midk
                maxk=midk-1
            else:
                mink=midk+1
        
        return ans