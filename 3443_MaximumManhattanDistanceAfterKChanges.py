class Solution:
    def maxDistance(self, s: str, k: int) -> int:
    
        horizontal,vertical, maxDistance = 0, 0, 0

        for i in range(len(s)):
            if s[i]=='N':
                vertical+=1
            elif s[i]=='S':
                vertical-=1
            elif s[i]=='E':
                horizontal+=1
            else:
                horizontal-=1
            
            maxDistance = max(maxDistance, min( i+1, abs(vertical) + abs(horizontal) + 2*k ))
    
        return maxDistance

    
# class Solution:
#     def maxDistance(self, s: str, k: int) -> int:
        
#         def maxDistanceWithPrefered(prefV, prefH, toChangeV, toChangeH)-> int:
#             newK = k
#             currDistance, maxDistance = 0, 0
#             for c in s:
#                 if c==prefV or c==prefH:
#                     currDistance+=1
#                 elif c==toChangeV or c==toChangeH:
#                     if newK >0:
#                         newK-=1
#                         currDistance+=1
#                     else:
#                         currDistance-=1
                
#                 maxDistance = max(maxDistance, currDistance)
            
#             return maxDistance


#         return max(maxDistanceWithPrefered( 'N','E', 'S','W'), maxDistanceWithPrefered( 'N','W', 'S','E'), maxDistanceWithPrefered( 'S','E', 'N','W'), maxDistanceWithPrefered( 'S','W', 'N','E'))


print(Solution().maxDistance(s = "NWSE", k = 1))
print(Solution().maxDistance(s = "NSWWEW", k = 3))