from typing import List
from collections import deque

# tc=O(n*l + n*l*26*l)=O((l^2) *n)
# sc=O((l^2)*n)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if beginWord==endWord or endWord not in wordSet:
            return 0

        l = len(beginWord)
        # n = len(wordList)

        dist = 0
        q = deque([beginWord])

        while q:
            dist+=1
            for _ in range(len(q)):

                word = q.popleft()

                for i in range(l):
                    for c in range(97, 123):
                        if chr(c)==word[i]:
                            continue
                        
                        nxtWord = word[:i] + chr(c) + word[i+1:]

                        if nxtWord in wordSet:
                            if nxtWord==endWord:
                                return dist+1
                            q.append(nxtWord)
                            wordSet.remove(nxtWord)
        
        return 0