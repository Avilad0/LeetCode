class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7
        
        self.memo = {}
        self.freq = [0]*10
        
        self.prefixCountSum = [0]*10

        self.factorial = [1]*41 #Maximum length of odd or even is 80/2 = 40
        for i in range(2,41):
            self.factorial[i] = (i*self.factorial[i-1])
        
    def combinationNCR(self, n, r):
        return (self.factorial[n] // (self.factorial[r]*self.factorial[n-r]) )%self.MOD

    def dfs(self, currDigit, currOddSum, oddNumUsed) -> int:

        if (currDigit,currOddSum,oddNumUsed) in self.memo:
            return self.memo[(currDigit,currOddSum,oddNumUsed)]

        evenNumUsed = 0
        if currDigit>0:
            evenNumUsed = self.prefixCountSum[currDigit-1]-oddNumUsed

        if currDigit>9 and oddNumUsed == self.oddCount and currOddSum==self.targetSum:
            return 1
        
        if currDigit>9 or oddNumUsed>self.oddCount or evenNumUsed>self.evenCount or currOddSum>self.targetSum:
            return 0
        
        oddPlacesRemaining = self.oddCount - oddNumUsed
        evenPlacesRemaining = self.evenCount - evenNumUsed
        minOddSelectionsRequired = max(0, self.freq[currDigit] - evenPlacesRemaining)
        maxOddSelectionsRequired = min(self.freq[currDigit], oddPlacesRemaining)

        ans = 0
        for currNumCount in range( minOddSelectionsRequired, maxOddSelectionsRequired+1):
            waysToPlaceCurrNumCount = self.combinationNCR(oddPlacesRemaining, currNumCount)  # Odd Pos Placements
            waysToPlaceCurrNumCount = (waysToPlaceCurrNumCount * self.combinationNCR(evenPlacesRemaining, self.freq[currDigit] - currNumCount))%self.MOD  # Even pos Placements

            ans = (ans + (waysToPlaceCurrNumCount*self.dfs(currDigit+1, currOddSum + (currNumCount*currDigit), oddNumUsed+currNumCount)))%self.MOD
        

        self.memo[(currDigit,currOddSum, oddNumUsed)] = ans
        return ans
        

    def countBalancedPermutations(self, num: str) -> int:
        
        self.n = len(num)
        self.oddCount = self.n//2
        self.evenCount = self.n - self.oddCount

        total = 0
        
        for digitChar in num:
            digit = ord(digitChar)-48
            self.freq[digit]+=1
            total += digit
        
        if total%2:
            return 0
        
        self.prefixCountSum[0]=self.freq[0]
        for i in range(1,10):
            self.prefixCountSum[i] = self.prefixCountSum[i-1] + self.freq[i]
        
        self.targetSum = total//2

        return self.dfs(0, 0, 0)
        

# print(Solution().countBalancedPermutations(num ="123")) #2
# print(Solution().countBalancedPermutations(num ="434056")) #36
print(Solution().countBalancedPermutations(num ="00000000000000000000000000000000000000000000000000000000000000000000000000000000")) #1


'''
344 056
waysToplace 344 = 3*1
waysToPlace 056  = 3*2*1 

034456

starting from 0 for odd place:
3*2*1 * 3*1

starting from 3 for odd place:
3*1 * 3*2*1

total = 18*2 = 36
'''