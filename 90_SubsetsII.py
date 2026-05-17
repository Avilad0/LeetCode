from typing import List

# tc= O(n∗(2^n)), sc = O(n) [2^n for output], - backtracking using sorting - same as below
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:        
        n = len(nums)
        nums.sort()

        ans = []
        stack = []
        def backtrack(i):
            ans.append(stack[:])
        
            
            for j in range(i, n):
                if j>i and nums[j]==nums[j-1]:
                    continue
                stack.append(nums[j])
                backtrack(j+1)
                stack.pop()
        
        backtrack(0)
        return ans


# tc= O(n∗(2^n)), sc = O(n) [2^n for output], - backtracking using freq - same as above
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:        
        freq = {}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        freq = [[num,freq[num]] for num in freq.keys() ]
        fn=len(freq)
        
        ans = []
        stack = []
        def backtrack(i):
            if i==fn:
                ans.append(stack[:])
                return
            
            backtrack(i+1)
            [num,f] = freq[i]
            for j in range(f):
                stack.append(num)
                backtrack(i+1)
            while stack and stack[-1]==num:
                stack.pop()
        
        backtrack(0)
        return ans