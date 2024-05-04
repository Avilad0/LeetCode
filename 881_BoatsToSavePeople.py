from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        ans =0 
        n = len(people)-1
        i=0

        while i<=n:
            if people[i] + people[n] <=limit:
                i+=1
                
            n-=1
            ans+=1


        return ans
    

print(Solution().numRescueBoats(people = [1,2], limit = 3)) #1
print(Solution().numRescueBoats(people = [3,2,2,1], limit = 3)) #3
print(Solution().numRescueBoats(people = [3,5,3,4], limit = 5)) #4
