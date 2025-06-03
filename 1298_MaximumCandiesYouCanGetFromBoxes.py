from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque(initialBoxes)

        isChanged = True
        maxCandies = 0
        while isChanged:
            qLen, isChanged = len(queue), False

            for _ in range(qLen):
                curr = queue.popleft()

                if status[curr]==0:
                    queue.append(curr)
                    continue

                isChanged = True

                maxCandies += candies[curr]

                for nxt in containedBoxes[curr]:
                    queue.append(nxt)
                
                for newKeys in keys[curr]:
                    status[newKeys] = 1

        return maxCandies