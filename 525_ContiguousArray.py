from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:


        map = {}
        count = 0
        ans = 0
        
        i=0
        for num in nums:
            if num==0:
                count-=1 
            else:
                count+=1
            
            if count == 0:
                ans = i + 1
            elif count not in map:
                map[count]=i
            else:
                ans = max(ans, i - map[count])
            
            i+=1

        return ans


        # DP : MEMORY EXCEED!!!!!!!!!!
        # dp = []
        # max = 0
        # l = len(nums)

        # for i in range(0,l-1):
        #     count=0
        #     dp.append([])
        #     for j in range(i,l):
        #         if nums[j]==0:
        #             count-=1
        #         else:
        #             count+=1
                
        #         dp[i].append(count)
                
        #         if count == 0 and max<(j-i+1):
        #             max = j-i+1
        #             if max == l:
        #                 return max
        
        # return max
    


