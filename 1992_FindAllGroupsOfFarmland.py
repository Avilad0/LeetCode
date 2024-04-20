from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        # faster than the dfs approach
        ans = []
        m = len(land)
        n = len(land[0])

        for i in range(m):
            for j in range(n):
                if land[i][j]==1 and (i==0 or land[i-1][j]==0) and (j==0 or land[i][j-1]==0):
                    k,l=i,j
                    
                    while k+1<m and land[k+1][j]==1:
                        k+=1
                    
                    while l+1<n and land[i][l+1]==1:
                        l+=1

                    ans.append([i,j,k,l])


        return ans


        # slower than the iterative approach
        # ans = []
        # m = len(land)
        # n = len(land[0])

        # def dfs(i,j,k)-> List[int]:
        #     if i>=m or j>=n or land[i][j]==0:
        #         return k
            
        #     land[i][j]=0

        #     k1 = dfs(i+1,j,[i,j])
        #     k2 = dfs(i,j+1,[i,j])
        #     return [max(k1[0],k2[0]) , max((k1[1],k2[1]))]


        # for i in range(m):
        #     for j in range(n):
        #         if land[i][j]==1:
        #             ans.append( [i,j] + dfs(i,j,[i,j]))


        # return ans
    

print(Solution().findFarmland([[0]]))
print(Solution().findFarmland([[1,1],[1,1]]))
print(Solution().findFarmland([[1,0,0],[0,1,1],[0,1,1]]))