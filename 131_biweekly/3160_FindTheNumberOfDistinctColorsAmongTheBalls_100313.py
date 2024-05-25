from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        c = {}
        colors_freq = {}
        ans = 0
        ans_list =[]
        for q in queries:
            if q[1] in colors_freq and colors_freq[q[1]]!=0:
                colors_freq[q[1]]+=1
            else:
                colors_freq[q[1]]=1
                ans+=1

            if q[0] in c:
                colors_freq[c[q[0]]]-=1
                if colors_freq[c[q[0]]]==0:
                    ans-=1
            
            c[q[0]]=q[1]
            
            ans_list.append(ans)

        return ans_list
    

print(Solution().queryResults(limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]))  #Output: [1,2,2,3]
