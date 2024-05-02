from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        check = [0]*1001
        for n in nums:
            if n>0:
                check[n]|=1
            else:
                n*=-1
                check[n]|=2

            if check[n]==3 and n>ans:
                ans = n
        
        return ans
        # ans = -1
        # check = {}
        # for n in nums:
        #     t=0
        #     if n>0:
        #         t|=1
        #     else:
        #         n*=-1
        #         t|=2

        #     if n not in check:
        #         check[n]=0
            
        #     check[n]|=t
        #     if check[n]==3 and n>ans:
        #         ans = n
        
        # return ans