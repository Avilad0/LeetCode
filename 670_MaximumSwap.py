class Solution:
    def maximumSwap(self, num: int) -> int:

        if num<10:
            return num
        
        numStr = list(str(num))
        n = len(numStr)
        swapIndex1,swapIndex2 = -1,-1
        maxIndex = n-1

        for i in range(n-2,-1,-1):
            if numStr[i]>numStr[maxIndex]:
                maxIndex=i
            elif numStr[i]<numStr[maxIndex]:
                swapIndex1,swapIndex2 = maxIndex, i
        
        if swapIndex1!= -1:
            numStr[swapIndex1], numStr[swapIndex2] = numStr[swapIndex2], numStr[swapIndex1]

        return int("".join(numStr))
    

# wrong after 105/112
# class Solution:
#     def maximumSwap(self, num: int) -> int:
        
#         arr =[]
#         l=0
#         while num:
#             arr.append([num%10,l])
#             num//=10
#             l+=1
        
#         arr_unsorted = arr.copy()
#         arr.sort(key=lambda x:(x[0],-x[1]))

#         l-=1
#         while l>=0 and arr_unsorted[l][0]==arr[l][0]:
#             l-=1

        
#         if l>=0:
#             arr_unsorted[l][0] , arr_unsorted[arr[l][1]][0] = arr[l][0], arr_unsorted[l][0]

#         num =0
#         arr_unsorted.reverse()
#         for n in arr_unsorted:
#             num = num*10 + n[0]

#         return num
        
# print(Solution().maximumSwap(2736))
# print(Solution().maximumSwap(1993)) #9913
print(Solution().maximumSwap(98368)) #98863




'''
Input: num = 2736
[[6,0], [3,1], [7,2], [2,3]]
[[2,3], [3,1], [6,0], [7,2]]

swap:
[2,3] < [7,2]
[7,2] < [2,3]

[[6,0], [3,1], [2,3], [7,2]]

Output: 7236
'''