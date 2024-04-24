class Solution:
    def tribonacci(self, n: int) -> int:

        t=[0,1,1]

        for i in range(3,n+1):
            t[i%3] = t[0]+t[1]+t[2]

        return t[n%3]
    

print(Solution().tribonacci(1))