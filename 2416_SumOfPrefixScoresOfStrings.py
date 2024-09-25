from typing import List

class TrieNode:
    def __init__(self):
        self.next = [None]*26
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        n = len(words)
        root = self.buildTrie(words)

        return [self.count(words[i], root) for i in range(n)]
    
    def count(self, s: str, root: TrieNode):
        node = root
        ans = 0
        for c in s:
            ans += node.next[ord(c) - ord("a")].count
            node = node.next[ord(c) - ord("a")]
        return ans

    
    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if not node.next[ord(char)-ord('a')]:
                    node.next[ord(char)-ord('a')] = TrieNode()
                node.next[ord(char) - ord('a')].count += 1
                node = node.next[ord(char) - ord('a')]
        return root