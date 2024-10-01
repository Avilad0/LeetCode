from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        kRemainders = [0 for _ in range(k)]
        
        for num in arr:
            rem = ((num%k)+k)%k
            remK = 0 if rem==0 else k-rem
            if kRemainders[remK] > 0:
                kRemainders[remK]-=1
            else:
                kRemainders[rem]+=1
            
        return sum(kRemainders) == 0 
    
print(Solution().canArrange([1,2,3,4,5,10,6,7,8,9], 5)) #True