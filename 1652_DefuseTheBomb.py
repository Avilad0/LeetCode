from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k ==0 :
            return [0]*len(code)
        
        n=len(code)
        ans = [0]
        if k>0:
            for i in range(1,k+1):
                ans[0]+=code[i]
            
            for i in range(1,n):
                ans.append(ans[-1] - code[i] + code[(i+k)%n])
        else:
            for i in range(n-1,n-1+k,-1):
                ans[0]+=code[i]

            for i in range(1,n):
                ans.append(ans[-1] + code[i-1] - code[(i+k+n-1)%n])

        return ans
    
    
# print(Solution().decrypt(code = [5,7,1,4], k = 3))  #Output: [12,10,16,13]
print(Solution().decrypt( code = [2,4,9,3], k = -2)) # Output: [12,5,6,13]
