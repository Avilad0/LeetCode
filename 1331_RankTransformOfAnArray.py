from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        uniqueArr = sorted(list(set(arr)))
        rankMap = { uniqueArr[i]:(i+1) for i in range(len(uniqueArr))}

        return [ rankMap[arr[i]] for i in range(len(arr))]