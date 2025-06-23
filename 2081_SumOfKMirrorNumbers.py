class Solution:
    def kMirror(self, k: int, n: int) -> int:
        num, summ, count = 1, 0, 0

        while count<n:
            start, end = num, num*10
            for isEven in range(2):
                for curr in range(start, end):
                    currStr = str(curr)

                    if isEven:
                        currNum = int(currStr + currStr[-1::-1])
                    else:
                        currNum = int(currStr + currStr[-2::-1])

                    baseK = self.convertToBaseK(currNum, k)
                    if self.isMirror(baseK):
                        summ+=currNum
                        count+=1
                        if count==n:
                            return summ
            num*=10

        return summ
    

    def convertToBaseK(self, num, k):
        if num == 0:
            return "0"

        digits = "0123456789"
        result = []

        while num > 0:
            remainder = num % k
            result.append(digits[remainder])
            num //= k
        
        result.reverse()
        return "".join(result)
    

    def isMirror(self, num):
        n = len(num)
        for i in range(n//2):
            if num[i]!=num[n-i-1]:
                return False
        
        return True



# class Solution:
#     def kMirror(self, k: int, n: int) -> int:
#         curr, summ, count = 0, 0, 0

#         while count<n:
#             curr = self.getNextBase10Mirror(curr)

#             baseK = self.convertToBaseK(curr, k)
#             if self.isMirror(baseK):
#                 summ+=curr
#                 count+=1

#         return summ
    
#     def getNextBase10Mirror(self, num):
#         strNum = list(str(num))
#         n = len(strNum)

#         i = (n-1)//2
#         while i>=0 and strNum[i]=='9':
#             i-=1
        
#         if i<0:
#             return 10**n + 1
        
#         strNum[i] = strNum[n-i-1] = str(int(strNum[i]) + 1)
#         i+=1
#         while i<= (n-1)//2:
#             strNum[i] = "0"
#             strNum[n-i-1] = "0"
#             i+=1

#         return int("".join(strNum))

#     def convertToBaseK(self, num, k):
#         if num == 0:
#             return "0"

#         digits = "0123456789"
#         result = []

#         while num > 0:
#             remainder = num % k
#             result.append(digits[remainder])
#             num //= k
        
#         result.reverse()
#         return "".join(result)
    

#     def isMirror(self, num):
#         n = len(num)
#         for i in range(n//2):
#             if num[i]!=num[n-i-1]:
#                 return False
        
#         return True


print(Solution().kMirror(3,7))