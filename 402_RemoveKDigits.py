
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        l = len(num)
        if l == k:
            return '0'
        
        stack = []
        for i in range(l):
            while k>0 and stack and stack[-1]>num[i]:
                stack.pop()
                k-=1
            stack.append(num[i])
            
        if k>0:
            stack = stack[:-k]
        
        ans = "".join(stack).lstrip('0')
        
        return ans if ans else "0"


print(Solution().removeKdigits(num = "10", k = 1))
print(Solution().removeKdigits(num = "1432219", k = 3))
print(Solution().removeKdigits(num = "10200", k = 1))
print(Solution().removeKdigits(num = "10", k = 2))
print(Solution().removeKdigits(num = "143213219", k = 4))
