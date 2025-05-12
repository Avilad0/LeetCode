from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digitsFreq = [0]*10
        for d in digits:
            digitsFreq[d]+=1
        
        evenNums = []
        for i in range(1,10):
            if digitsFreq[i]==0:
                continue
            digitsFreq[i]-=1

            for j in range(10):
                if digitsFreq[j]==0:
                    continue
                digitsFreq[j]-=1

                for k in range(0,9,2):
                    if digitsFreq[k]==0:
                        continue
                    evenNums.append(i*100 + j*10 + k)

                digitsFreq[j]+=1

            digitsFreq[i]+=1
        
        return evenNums

# class Solution:
#     def findEvenNumbers(self, digits: List[int]) -> List[int]:
#         digitsFreq = [0]*10
#         for d in digits:
#             digitsFreq[d]+=1
        
#         evenNums = []
#         for num in range(100, 1000, 2):
#             currDigits = defaultdict(int)
#             temp = num
#             while temp:
#                 currDigits[temp%10]+=1
#                 temp//=10
            
#             isEven = True
#             for (d,f) in currDigits.items():
#                 if digitsFreq[d]<f:
#                     isEven = False
#                     break
            
#             if isEven:
#                 evenNums.append(num)
        
#         return evenNums

