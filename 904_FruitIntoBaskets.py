from typing import List

# 1-pass
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n=len(fruits)
        type1, type2 = -1,-1
        nextleft, left = 0, 0
        maxFruits = 0

        for right in range(n):
            if fruits[right]!=type1 and fruits[right]!=type2:
                maxFruits = max(maxFruits, right-left)
                left=nextleft
                nextleft=right
                if fruits[left]!=type1:
                    type1=fruits[right]
                else:
                    type2=fruits[right]
            elif fruits[right]!=fruits[right-1]:
                nextleft=right

        maxFruits = max(maxFruits, n-left)

        return maxFruits



# # 2-pass
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:

#         n=len(fruits)

#         type1, type2 = -1,-1
#         type1Freq, type2Freq = 0,0

#         left = 0
#         maxFruits = 0

#         for right in range(n):
#             if fruits[right]==type1:
#                 type1Freq+=1
#             elif fruits[right]==type2:
#                 type2Freq+=1
#             else:
#                 maxFruits = max(maxFruits, right-left)
#                 while type1Freq!=0 and type2Freq!=0:
#                     if fruits[left]==type1:
#                         type1Freq-=1
#                     else:
#                         type2Freq-=1
#                     left+=1

#                 if type1Freq==0:
#                     type1=fruits[right]
#                     type1Freq=1
#                 else:
#                     type2=fruits[right]
#                     type2Freq=1
        
#         maxFruits = max(maxFruits, n-left)

#         return maxFruits