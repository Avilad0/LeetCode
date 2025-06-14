class Solution:
    def minMaxDifference(self, num: int) -> int:
        strNum = str(num)

        n, i = len(strNum),0
        while i<n and strNum[i]=='9':
            i+=1
        
        if i == n:
            maxNum = num
        else :
            maxNum = int(strNum.replace(strNum[i],'9'))
            
        minNum = int(strNum.replace(strNum[0],'0'))

        return maxNum - minNum