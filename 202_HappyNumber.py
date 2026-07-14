# tc = O(logn), sc=O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(x):
            newX = 0
            while x:
                rem = x%10
                x=x//10
                newX+= (rem*rem)

            return newX
        
        slow, fast = n,n
        while True:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
            if fast==1 or slow==fast:
                break

        return fast==1
    
# # tc = O(logn), sc=O(logn)
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = set([n])
#         x=n
#         while x!=1:
#             newX = 0
#             while x:
#                 rem = x%10
#                 x=x//10
#                 newX+= (rem*rem)
#             if newX in seen:
#                 return False
#             x=newX
#             seen.add(x)

#         return True

