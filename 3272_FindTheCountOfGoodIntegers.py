class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        start = 10**((n-1)//2)
        end = start*10
        reverseStartIndex = n&1 #skip last digit while appending in reverse, if n is odd

        sortedKPalindromes = set()
        for i in range(start, end):
            s = str(i)
            s = s + s[::-1][reverseStartIndex:]
            
            if int(s)%k==0:
                sortedKPalindromes.add( "".join(sorted(s)))
        
        factorial = [1]
        for i in range(1, n+1):
            factorial.append(factorial[-1]*i)

        ans = 0
        for s in sortedKPalindromes:
            digitCounts = [0]*10
            for c in s:
                digitCounts[int(c)] +=1
            
            combinations = (n-digitCounts[0])*factorial[n-1]
            for count in digitCounts:
                combinations //= factorial[count]

            ans += combinations

        return ans
    

print(Solution().countGoodIntegers(3,5)) #27