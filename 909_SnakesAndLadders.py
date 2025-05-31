from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n*n

        visited = [[False]*n for _ in range(n)]
        visited[n-1][0] = True
        queue = deque([(0,1)]) #cost,node

        while queue:
            (cost, node) = queue.popleft()

            for nxtNode in range(node+1, min(node+6, target) + 1):
                
                i = n-1 - ((nxtNode-1)//n)
                j = (nxtNode-1)%n
                if ((nxtNode-1)//n)%2==1:
                    j = n-1 - j

                if visited[i][j]:
                    continue
                
                visited[i][j] = True

                nxt = nxtNode
                if board[i][j]!=-1:
                    nxt = board[i][j]           

                if nxt == target:
                    return cost+1     

                queue.append((cost+1, nxt))

        return -1


# print(Solution().snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]])) #4
print(Solution().snakesAndLadders(board = [[-1,-1,-1],[-1,9,8],[-1,8,9]])) #1

'''
n=5

0 = (n-1,0)
14 = (n-3,1)

10 = (n-2, n-4)
'''