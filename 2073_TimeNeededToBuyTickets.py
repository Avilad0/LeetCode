from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        ans = 0
        for i in range(0,k+1):
            ans+=min(tickets[k], tickets[i])

        for i in range(k+1,len(tickets)):
            ans+=min(tickets[k]-1, tickets[i])

        return ans

        # ans = 0
        # while tickets[k]!=0:

        #     for i in range(len(tickets)):
        #         if tickets[i]!=0:
        #             tickets[i]-=1
        #             ans+=1
        #         if tickets[k]==0:
        #             break

        # return ans
    

print(Solution().timeRequiredToBuy(tickets = [5,1,1,1], k = 0))
print(Solution().timeRequiredToBuy(tickets = [2,3,2], k = 2))