from typing import List

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
        blocks = [0]
        ans =[]
        l=1
        for q in queries:
            if q[0]==1:
                i=1
                while i<l and blocks[i]<q[1]:
                    i+=1
                blocks.insert(i,q[1])
                l+=1
            
            else:
                i=1
                find = False
                while i<l and blocks[i]<q[1]:
                    if q[2]<=blocks[i]-blocks[i-1]:
                        find=True
                        break
                    i+=1
                
                if i==l or not find:
                    if q[2]<= q[1] - blocks[i-1]:
                        find = True
                
                ans.append(find)
                    

        return ans
    




print(Solution().getResults(queries = [[1,4],[2,1,2]]))  #Output: [false]

print(Solution().getResults(queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]))  #Output: [false,true,true]
print(Solution().getResults(queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]))  #Output: [true,true,false]

