from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n = len(box), len(box[0])
        for row in box:
            stones=0
            for j in range(n):
                if row[j]=='#':
                    stones+=1
                    row[j]='.'
                elif row[j]=='*':
                    for i in range(j-1,j-stones-1,-1):
                        row[i]='#'
                    stones=0
            for i in range(n-1,n-stones-1,-1):
                row[i]='#'
        
        rotated = []
        for i in range(n):
            rotated.append([])
            for j in range(m):
                rotated[i].append(box[m-1-j][i])

        return rotated


print(Solution().rotateTheBox(box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]))
'''
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
'''


'''
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

0,0 = 1,0
0,1 = 0,0
1,0 = 1,1
1,1 = 0,1
2,0 = 1,2
2,1 = 0,2
3,0 = 1,3
3,1 = 0,3
         
'''