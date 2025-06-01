# tc = O(1)
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        def nC2(x):
            return 0 if x<0 else (x*(x-1))//2
            
        return nC2(n+2) - 3*nC2(n+2 -(limit+1)) + 3*nC2(n+2 -2*(limit+1)) - nC2(n+2 -3*(limit+1))
        
        # total possible combinations 
        # - 3*(1 child with more than limit) 
        # + 3*(2 child with more than limit [repeated combinations in previous case]) 
        # - (3 child with more than limit)


# # tc = O(min(n,limit))
# class Solution:
#     def distributeCandies(self, n: int, limit: int) -> int:

#         if n/3 > limit:
#             return 0

#         count = 0
#         for i in range(min(n,limit) +1):
#             remaining = n-i
#             if remaining/2 <= limit:
#                 if remaining <= limit:
#                     count += remaining + 1
#                 else:                        
#                     remaining -= limit
#                     count += limit - remaining + 1
        
#         return count

print(Solution().distributeCandies(n=5, limit=2))
print(Solution().distributeCandies(n=3, limit=3))