class Solution:
    def maxDiff(self, num: int) -> int:
        strNum = str(num)

        n, i = len(strNum),0
        while i<n and strNum[i]=='9':
            i+=1
        
        if i == n:
            maxNum = num
        else:
            maxNum = int(strNum.replace(strNum[i],'9'))


        i = 0
        while i<n and (strNum[i]=='1' or strNum[i]=='0'):
            i+=1

        if i == n:
            minNum = num
        elif i==0:
            minNum = int(strNum.replace(strNum[i],'1'))
        else:
            minNum = int(strNum.replace(strNum[i],'0'))

        return maxNum - minNum
    
'''
num = 1101057, ans = 8808050

maxNum = 9909057
minNum = 1101007

'''
