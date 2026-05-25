from typing import List
from collections import deque, defaultdict


# Time complexity: O(N * L^2 + S) where N = number of words in `wordList`,
# L = length of each word, and S is the cost to build/output all shortest sequences.
# Space complexity: O(N * L)
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        availableWords = set(wordList)
        availableWords.discard(beginWord)

        prevWords = defaultdict(set)
        minDistance = {beginWord:0}

        queue = deque([beginWord])
        currDist = 0
        isTargetFound = False

        while queue and not isTargetFound:
            currDist+=1

            for _ in range(len(queue)):
                currWord = queue.popleft()

                for i in range(len(currWord)):
                    for j in range(97,123):
                        newChr = chr(j)
                        if newChr==currWord[i]:
                            continue

                        nextWord = currWord[:i]+ newChr + currWord[i+1:]
                        if nextWord not in minDistance or minDistance[nextWord]==currDist:
                            prevWords[nextWord].add(currWord)

                        if nextWord in availableWords:
                            if nextWord==endWord:
                                isTargetFound=True

                            availableWords.discard(nextWord)
                            queue.append(nextWord)
                            minDistance[nextWord] = currDist
        

        if not isTargetFound:
            return []

        ans = []
        stack = [endWord]

        def dfs(curr):
            if curr==beginWord:
                ans.append(stack[::-1])
                return
            
            for prev in prevWords[curr]:
                stack.append(prev)
                dfs(prev)
                stack.pop()
        
        dfs(endWord)
        return ans