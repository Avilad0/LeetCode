from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mostNum1, mostNum2, mostNum1Count, mostNum2Count = None, None, 0, 0

        for num in nums:
            if mostNum1==num:
                mostNum1Count+=1            
            elif mostNum2==num:
                mostNum2Count+=1

            elif mostNum1Count==0:
                mostNum1 = num
                mostNum1Count=1
            elif mostNum2Count==0:
                mostNum2 = num
                mostNum2Count=1

            else:
                mostNum1Count-=1
                mostNum2Count-=1
        
        reCount1, reCount2 = 0, 0
        for num in nums:
            if num==mostNum1:
                reCount1+=1
            elif num==mostNum2:
                reCount2+=1
        
        n3 = len(nums)//3
        ans  = []
        if reCount1>n3:
            ans.append(mostNum1)
        if reCount2>n3:
            ans.append(mostNum2)

        return ans