from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        visited = set([startGene])
        queue = [(startGene,0)]
        while queue:
            (currGene, currMoves) = queue.pop(0)

            for gene in bank:                
                if gene in visited:
                    continue

                diffs = 0
                for i in range(8):
                    if currGene[i] != gene[i]:
                        diffs+=1
                
                if diffs==1:
                    if gene==endGene:
                        return currMoves+1
                    
                    queue.append((gene,currMoves+1))
                    visited.add(gene)
        
        return -1


# print(Solution().minMutation(startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]))
print(Solution().minMutation(startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))