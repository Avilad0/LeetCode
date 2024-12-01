from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sett = set()
        for n in arr:
            if n*2 in sett or (n%2==0 and (n/2) in sett):
                return True
            sett.add(n)

        return False          