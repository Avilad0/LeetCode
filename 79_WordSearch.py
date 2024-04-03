from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word)
        m = len(board)
        n = len(board[0])
        
        if m*n<l:
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.search(board,word,m,n,l,i,j,1):
                        return True
                    
        return False
    


    def search(self, board: List[List[str]], word: str,m,n,l,i,j,k) -> bool:
        if k==l:
            return True
        
        check=False

        temp = board[i][j]
        board[i][j] = ''


        if i<m-1 and board[i+1][j]==word[k]:
            check = check | self.search(board,word,m,n,l,i+1,j,k+1)

        if (not check) and i>0 and board[i-1][j]==word[k]:
            check = check | self.search(board,word,m,n,l,i-1,j,k+1)
        
        if (not check) and j<n-1 and board[i][j+1]==word[k]:
            check = check | self.search(board,word,m,n,l,i,j+1,k+1)

        if (not check) and j>0 and board[i][j-1]==word[k]:
            check = check | self.search(board,word,m,n,l,i,j-1,k+1)


        board[i][j] = temp
        return check