from typing import List

# m=rows, n=cols, t=max len of word, s=sum(len of all words)
# Time complexity: O(m∗n∗4∗3^(t-1)+s)
# Space complexity: O(s)O(s)
class TrieNode:
    def __init__(self):
        self.trieMap = {}
        self.isWordEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr= self.root
        for c in word:
            if c not in curr.trieMap:
                curr.trieMap[c] = TrieNode()

            curr = curr.trieMap[c]
        
        curr.isWordEnd = True    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for word in words:
            trie.add(word)
        
        dirs = ((0,1),(1,0),(0,-1),(-1,0))
        m,n = len(board), len(board[0])
        ans = []
        stck = []

        def backtrack(i,j, trieNode):
            # print(i,j,trieNode.trieMap)
            if trieNode.isWordEnd:
                ans.append("".join(stck))
                trieNode.isWordEnd = False

            if i<0 or i>=m or j<0 or j>=n or board[i][j] not in trieNode.trieMap:
                return

            stck.append(board[i][j])
            board[i][j]=''
            for (di,dj) in dirs:
                backtrack(i+di, j+dj, trieNode.trieMap[stck[-1]])

            board[i][j]=stck.pop()

        for i in range(m):
            for j in range(n):
                backtrack(i,j,trie.root)
        
        return ans