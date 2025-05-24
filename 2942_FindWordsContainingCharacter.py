from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indexes = []
        for i in range(len(words)):
            if x in words[i]:
                indexes.append(i)

        return indexes