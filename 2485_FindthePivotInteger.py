# import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        
        totalSum = int(n*(n+1)/2)
        for i in range(int(n/2) , n+1):
            sum1= int(i*(i+1)/2)
            sum2 = totalSum - sum1 + i

            if sum1 == sum2:
                return i
            
        return -1

        # twiceSum = int(n*(n+1)/2)
        # if twiceSum%2!=0:
        #     return -1
        
        # expectedSum = int(twiceSum/2)

        # x1 = int((-1 + math.sqrt(1 + 4*twiceSum))/2)
        # x2 = int((-1 - math.sqrt(1 + 4*twiceSum))/2)

        # if x1 * (x1+1) == twiceSum:
        #     return x1
        # elif x2 * (x2+1) == twiceSum:
        #     return x2
        # else:
        #     return -1
        
        # # x(x+1)/2 = expectedSum 
        # # x^2 + x = 2*expectedSum
        # # x^2 + x - 2*expectedSum = 0




