from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        map = {score[i]:i for i in range(n)}
        ans = [""]*n
        
        score.sort(reverse=True)

        for i in range(n):
            
            if i>2:
                ans[map[score[i]]] = str(i+1)
            elif i==0:
                ans[map[score[i]]] = "Gold Medal"
            elif i==1:
                ans[map[score[i]]] = "Silver Medal"
            elif i==2:
                ans[map[score[i]]] = "Bronze Medal"
            

        return ans


print(Solution().findRelativeRanks(score = [5,4,3,2,1]))
print(Solution().findRelativeRanks([10,3,8,9,4]))