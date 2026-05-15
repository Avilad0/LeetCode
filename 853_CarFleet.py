from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        carSorted = sorted([(position[i], speed[i]) for i in range(n)])
    
        fleets = 0

        right = n-1
        while right>=0:
            currHours = (target-carSorted[right][0])/carSorted[right][1]
            left = right-1
            while left>=0 and carSorted[left][0]+(carSorted[left][1]*currHours) >= target:
                left-=1
            
            right=left
            fleets+=1

        return fleets