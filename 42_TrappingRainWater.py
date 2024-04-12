from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l<=2:
            return 0
        
        ans = 0
        temp_ans = 0
        h_in = 0
        for i in range(1,l):
            if height[i]>=height[h_in]:
                ans += temp_ans
                temp_ans=0
                h_in = i
            else:
                temp_ans+=height[h_in] - height[i]

        if temp_ans>0:
            m = height[l-1]
            for i in range(l-2,h_in,-1):
                if height[i]>m:
                    m = height[i]
                else:
                    ans+= m - height[i]
        return ans
    

print(Solution().trap([2,0,2]))
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([4,2,0,3,2,5]))