from typing import List

# tc=O(n!*n), sc=O(n) [(n!*n) for output list] - similar to below without visited and using swapping instead of stack
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = []
        temp = nums[:]

        def backtrack(i):
            if i==n:
                ans.append(temp[:])
            
            for j in range(i,n):
                temp[i], temp[j]=temp[j], temp[i]
                backtrack(i+1)
                temp[i], temp[j]=temp[j], temp[i]
            
        backtrack(0)
        return ans

# tc=O(n!*n), sc=O(n) [(n!*n) for output list]
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = []
        visited = [False]*n
        stack = []

        def backtrack(i):
            if i==n:
                ans.append(stack[:])
            
            for j in range(n):
                if not visited[j]:
                    visited[j]=True
                    stack.append(nums[j])
                    backtrack(i+1)
                    stack.pop()
                    visited[j]=False
            
        backtrack(0)
        return ans