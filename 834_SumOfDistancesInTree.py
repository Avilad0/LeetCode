from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(n)}
        ans = [0]*n
        count = [0]*n
        
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        def countDFS(node, prev):
            count[node]=1
            for child in graph[node]:
                if child !=prev:
                    countDFS(child,node)
                    count[node]+=count[child]
                    ans[node]+= ans[child] + count[child]

        def dfs(node, prev):
            for child in graph[node]:
                if child != prev:
                    # (ans[node] - count[child]) + (n - count[child])
                    ans[child] = ans[node] - (2*count[child]) + n 
                    dfs(child, node)

        countDFS(0,-1)
        dfs(0,-1)

        return ans


#  memory limit exceed in 4/74 cases
# class Solution:
#     def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
#         ans = [0]*n
#         graph = {i:[] for i in range(n)}
        
#         for e in edges:
#             graph[e[0]].append(e[1])
#             graph[e[1]].append(e[0])
#         memo ={}
#         for node in range(n):
#             ans[node] = self.calc(graph, 1, -1,node,memo)

#         return ans
    
#     def calc(self, graph, depth, previous ,node, memo):
#         if (previous,node,depth) in memo:
#             return memo[(previous,node,depth)]
        
#         ans = 0
#         for i in graph[node]:
#             if previous!=i:
#                 ans += depth + self.calc(graph, depth+1, node, i,memo)

#         memo[(previous,node,depth)] = ans
#         return ans
    

print(Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))

print(Solution().sumOfDistancesInTree(2, [[1,0]]))
print(Solution().sumOfDistancesInTree(1, []))