from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""
        candidate = sorted([c for c, w in Counter(s).items() if w >= k], reverse=True)

        queue = deque(candidate)
        while queue:
            curr = queue.popleft()
            if len(curr) > len(ans):
                ans = curr
            
            for c in candidate:
                nxt = curr + c
                it = iter(s)
                if all(ch in it for ch in nxt*k):
                    queue.append(nxt)
        return ans
    

print(Solution().longestSubsequenceRepeatedK(s = "letsleetcode", k = 2))  #"let"