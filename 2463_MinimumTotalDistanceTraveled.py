# from typing import List

# class Solution:
#     def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
#         fn, rn = len(factory), len(robot)
#         robot.sort()
#         factory.sort(key= lambda x:x[0])
#         factory2 = [factory[0]]
#         if fn>1:
#             factory2.append(factory[1])

#         steps = 0
#         for r in range(rn):
#             if robot[r] < factory2[0][0]:
#                 if factory2[0][1]==1:
#                     factory2 = factory2[1]
#                 else:
#                     factory2[0][1]-=1