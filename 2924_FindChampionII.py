from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        setPlayers = set([i for i in range(n)])

        for e in edges:
            if e[1] in setPlayers:
                setPlayers.remove(e[1])
        
        if len(setPlayers)==1:
            return setPlayers.pop()
        else:
            return -1