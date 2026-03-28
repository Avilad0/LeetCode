class Solution:
    def isValid(self, s: str) -> bool:
        openToCloseMap = {'(':')', '{':'}', '[':']'}

        stck = []
        for c in s:
            if c in openToCloseMap:
                stck.append(c)
            else:
                if stck and openToCloseMap[stck[-1]] == c:
                    stck.pop()
                else:
                    return False
        
        return not stck   