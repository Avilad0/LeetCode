class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        
        currStr = self.countAndSay(n-1)
        newStr, currChar, currCount = [], currStr[0], 0
        for c in currStr:
            if c==currChar:
                currCount+=1
            else:
                newStr.append(str(currCount))
                newStr.append(currChar)
                currCount=1
                currChar=c
        
        newStr.append(str(currCount))
        newStr.append(currChar)

        return "".join(newStr)