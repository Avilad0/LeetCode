class Solution:
    def maxDepth(self, s: str) -> int:
        max = 0
        count=0
        for c in s:
            if c=="(":
                count+=1
                if count>max:
                    max=count
            elif c==")":
                count-=1
        return max