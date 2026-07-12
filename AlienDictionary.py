from typing import List
from collections import  deque

# same complexity using topological sort, easier to implement
# tc = O(N+V+E), sc=O(V+E), N=sum of len of all words, V=Unique Chars, E=edges between unique chars
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adjList = {c: set() for word in words for c in word}       #firstCh -> nextCh
        indegree = {c:0 for c in adjList.keys()}

        for i in range(n-1):
            word1, word2 = words[i], words[i+1]

            if len(word1)>len(word2) and word1.startswith(word2):
                return ""
            
            minLen = min(len(word1), len(word2))
            for i in range(minLen):
                if word1[i]!=word2[i]:
                    if word2[i] not in adjList[word1[i]]:
                        adjList[word1[i]].add(word2[i])
                        indegree[word2[i]]+=1
                    break
            
        q =deque()
        for c in indegree.keys():
            if indegree[c]==0:
                q.append(c)

        ans = []
        while q:
            c = q.popleft()
            ans.append(c)
            for nxt in adjList[c]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    q.append(nxt)
        
        if len(indegree)!=len(ans):
            return ""

        return "".join(ans)



# class Solution:
#     def foreignDictionary(self, words: List[str]) -> str:
#         n = len(words)
#         adjList = {c: set() for word in words for c in word}     #firstCh -> nextCh

#         for i in range(n-1):
#             word1, word2 = words[i], words[i+1]

#             if len(word1)>len(word2) and word1.startswith(word2):
#                 return ""
            
#             minLen = min(len(word1), len(word2))
#             for i in range(minLen):
#                 if word1[i]!=word2[i]:
#                     adjList[word1[i]].add(word2[i])
#                     break
            
#         # key:True, key visited in curr cycle
#         # key:False, key visited but not in curr cycle
#         # !key : key not yet visited
#         visited = {}  

#         ansInRev = []
        
#         def dfs(curr):
#             if curr in visited:
#                 return visited[curr]

#             visited[curr] = True
#             for nxt in adjList[curr]:
#                 if dfs(nxt):
#                     return True
                
#             visited[curr] = False
#             ansInRev.append(curr)
        
#         for c in adjList:
#             if dfs(c):
#                 return ""
            
#         ansInRev.reverse()
#         return "".join(ansInRev)


            
        



'''
Input: ["hrn","hrf","er","enn","rfnn"]
Output: "hernf"

h -> e -> r
    r
        n -> f
    r -> n
        n
    f
        n
            n

list of mapping found = [h e r, r, n f, r n, n , f, n , n]

h = [e]
e = [r]
n = [f]
r = [n]


'''