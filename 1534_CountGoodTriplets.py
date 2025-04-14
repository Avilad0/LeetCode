from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        goodCount = 0
        n = len(arr)

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1, n):
                    if -a<= arr[i]-arr[j] <=a and -b<= arr[j]-arr[k] <=b and -c<= arr[k]-arr[i] <=c:
                        goodCount+=1
        
        return goodCount