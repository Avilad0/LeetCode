class Solution:

    ringLength = 0
    r2= 0
    keyLength = 0
    
    def findRotateSteps(self, ring: str, key: str) -> int:

        Solution.ringLength = len(ring)
        Solution.r2 = Solution.ringLength//2
        Solution.keyLength = len(key)

        map = {c:[] for c in ring}        
        for i in range(Solution.ringLength):
            map[ring[i]].append(i)

        return self.traverse(0,0,map,key,{})

    
    def traverse(self, ringIndex, keyIndex, map, key, memo):
        if keyIndex==Solution.keyLength:
            return 0
        
        if (keyIndex,ringIndex) in memo:
            return memo[(keyIndex,ringIndex)]

        ans = float('inf')
        for i in map[key[keyIndex]]:

            t= abs(ringIndex-i)
            t = t if t<=Solution.r2 else Solution.ringLength-t
             
            ans = min(ans, t+1+self.traverse(i, keyIndex+1,map, key, memo))

        memo[(keyIndex,ringIndex)]= ans
        
        return ans
    

print(Solution().findRotateSteps("caotmcaataijjxi","oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"))

print(Solution().findRotateSteps("abcde","ade"))
print(Solution().findRotateSteps("godding","gd"))
print(Solution().findRotateSteps("godding","godding"))
