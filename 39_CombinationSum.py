from typing import List

# Same complexity as below but better optimized to stop recursion early after sorting
# tc: O(2^(target/min(candidates))), sc: O(target/min(candidates))
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []

        def backtrack(i, currSum, currList):
            if currSum==target:
                ans.append(currList[:])
                return

            for j in range(i, n):
                if currSum+candidates[j]>target:
                    break
                currList.append(candidates[j])
                backtrack(j, currSum+candidates[j], currList)
                currList.pop()

        backtrack(0, 0, [])
        return ans
    

# # tc: O(2^(target/min(candidates))), sc: O(target/min(candidates))
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         n = len(candidates)
        
#         ans = []
#         def backtrack(i, currSum, currList):
#             if currSum==target:
#                 ans.append(currList[:])
#                 return

#             if currSum>target or i==n:
#                 return
            
#             backtrack(i+1, currSum, currList)

#             currList.append(candidates[i])
#             backtrack(i, currSum+candidates[i], currList)
#             currList.pop()

#         backtrack(0, 0, [])
#         return ans