from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = 1
        n = len(ratings)

        i=0
        while i<n-1:
            candies-=1
            
            increasingLen = 1
            while i<n-1 and ratings[i]< ratings[i+1]:
                increasingLen+=1
                i+=1
            
            equalsLen = 1
            while i<n-1 and ratings[i]==ratings[i+1]:
                equalsLen+=1
                i+=1

            decreasingLen = 1
            while i<n-1 and ratings[i]>ratings[i+1]:
                decreasingLen+=1
                i+=1

            if increasingLen<decreasingLen:
                increasingLen, decreasingLen = decreasingLen, increasingLen
            
            if equalsLen == 1:
                candies += ((increasingLen+1)*(increasingLen))//2 + ((decreasingLen)*(decreasingLen-1))//2
            else :
                candies += ((increasingLen+1)*increasingLen)//2 + ((decreasingLen+1)*decreasingLen)//2 + (equalsLen-2)

        return candies
    
    

print(Solution().candy(ratings = [1,0,2]))  #5
print(Solution().candy(ratings = [1,2,2]))  #4



'''
ratings : 1 2 3 3 2 6 3 2 2 1
candies : 1 2 3 2 1 3 2 1 2 1

'''