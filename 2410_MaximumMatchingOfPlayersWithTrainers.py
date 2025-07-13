from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ans = 0
        players.sort()
        trainers.sort()
        pI, tI = len(players)-1, len(trainers)-1

        while pI>=0 and tI>=0:
            if trainers[tI]>=players[pI]:
                ans+=1
                tI-=1
            pI-=1
        
        return ans