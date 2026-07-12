from typing import List
from collections import defaultdict, deque

# Hierholzer's Algorithm (iteration)
# tc = O(ElogE), sc = O(E)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        for src, dst in tickets:
            adjList[src].append(dst)
        
        for src in adjList.keys():
            adjList[src].sort(reverse=True)
        
        stack = ["JFK"]
        ans = []
        while stack:
            if adjList[stack[-1]]:
                stack.append(adjList[stack[-1]].pop())
            else:
                ans.append(stack.pop())            

        return ans[::-1]
    
# # Hierholzer's Algorithm (recursion)
# # tc = O(ElogE), sc = O(E)
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         adjList = defaultdict(list)
#         for src, dst in tickets:
#             adjList[src].append(dst)
        
#         for src in adjList.keys():
#             adjList[src].sort(reverse=True)
        
#         stack = []
#         def dfs(curr):
#             while adjList[curr]:
#                 nxt = adjList[curr].pop()
#                 dfs(nxt)
#             stack.append(curr)


#         dfs("JFK")
#         return stack[::-1]


# #TLE on leetcode, works on neetcode
# tc = O(E*V), sc = O(E*V)
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         adjList = defaultdict(list)
#         for src, dst in tickets:
#             adjList[src].append(dst)
        
#         for src in adjList.keys():
#             adjList[src].sort()
        
#         n=len(tickets)+1
#         stack = []
#         def dfs(curr):
#             stack.append(curr)
#             # print(stack)
#             if len(stack)==n:
#                 return 

#             for i in range(len(adjList[curr])):
#                 if adjList[curr][i]=="":
#                     continue
#                 temp = adjList[curr][i]
#                 adjList[curr][i] = ""
#                 dfs(temp)
#                 if len(stack)==n:
#                     return
#                 adjList[curr][i] = temp
#             stack.pop()

#         dfs("JFK")
#         return stack