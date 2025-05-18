from collections import defaultdict

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        validColPossibilities = defaultdict(list)

        totalFirstColCombinations = 3**m
        for combination in range(totalFirstColCombinations):
            curr = combination
            prev = -1
            colors = []
            for _ in range(m):
                if curr%3 == prev:
                    break
                prev = curr%3
                colors.append(curr%3)
                curr//=3
            else:
                validColPossibilities[combination] = colors
        
        
        validAdjacents = defaultdict(list)
        for mask1, color1 in validColPossibilities.items():
            for mask2, color2 in validColPossibilities.items():
                for i in range(m):
                    if color1[i]==color2[i]:
                        break
                else:
                    validAdjacents[mask1].append(mask2)
        

        dp = [int(mask in validColPossibilities) for mask in range(totalFirstColCombinations)]  # Count of each mask in curr column permutations

        for _ in range(n-1):
            nextDP = [0]*totalFirstColCombinations

            for mask1 in validColPossibilities:
                for mask2 in validAdjacents[mask1]:
                    nextDP[mask2]= (nextDP[mask2] + dp[mask1])%MOD
            
            dp = nextDP

            
        return sum(dp)%MOD
    

print(Solution().colorTheGrid(5,5)) #580986