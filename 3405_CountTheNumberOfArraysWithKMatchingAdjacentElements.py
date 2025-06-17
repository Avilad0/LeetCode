class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 +7

        def fastExponentiation(base, exp):
            ans = 1
            while exp:
                if exp&1:
                   ans = (ans * base)%MOD
                   exp-=1
                base = (base *base)%MOD
                exp//=2
            
            return ans


        def combinations(n, r):
            #nCr = n!/(r!(n-r)!)
            nfact = 1
            rFact, n_rFact = 1, 1
            for x in range(1,n+1):
                nfact= (nfact*x)%MOD
                
                if x == r:
                    rFact = nfact
                if x == n-r:
                    n_rFact = nfact
            
            #inverse(r!) = (fact[r]^(p-2)) % p
            return (nfact * (fastExponentiation(rFact, MOD-2)%MOD) * (fastExponentiation(n_rFact, MOD-2)%MOD) ) %MOD

        partitions = n-k
        count = (((m*fastExponentiation(m-1, partitions-1))%MOD) * combinations(n-1,k))%MOD 

        return count


# print(Solution().countGoodArrays(1,1,0))
print(Solution().countGoodArrays(n = 5581, m = 58624, k = 4766))


'''
total n-1 pairs, 
select k pairs to be same, therefore n-k-1 pairs will be different.

it means select n-k-1 partitions in arr where nums will change to something else.

So 1st partition will have m options and later partitions will have m-1 options as nums cannot be same as previous partition.

partitions = n-k
possibilities in each combination = m*((m-1)**(partitions-1))

total combinations  = Select n-k-1 points using as (n-1)C(n-k-1) 
                    = Same as Select k pairs using (n-1)C(k) [combinations formula]

total arrays possible = total combinations * possibilities in each combination
'''