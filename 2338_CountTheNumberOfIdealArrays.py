class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        MAX_N = 10**4 + 10
        MAX_P = 15

        sieve = [0]*MAX_N
        for i in range(2,MAX_N):
            if sieve[i]==0:
                for j in range(i, MAX_N, i):
                    sieve[j]= i
        
        prefixSum = [[] for _ in range(MAX_N)]

        for i in range(2, MAX_N):
            x = i
            while x>1:
                p = sieve[x]
                cnt = 0
                while x%p ==0:
                    x//=p
                    cnt+=1
                prefixSum[i].append(cnt)
        
        count = [[0]*(MAX_P + 1) for _ in range(MAX_N + MAX_P)]

        count[0][0] = 1

        for i in range(1, MAX_N+MAX_P):
            count[i][0] = 1
            for j in range(1, min(i, MAX_P)+1):
                count[i][j] = (count[i-1][j] + count[i-1][j-1])%MOD

        ans = 0
        for x in range(1, maxValue+1):
            mul = 1
            for p in prefixSum[x]:
                mul = mul*count[n+p-1][p]%MOD
            ans = (ans+mul)%MOD
        
        return ans