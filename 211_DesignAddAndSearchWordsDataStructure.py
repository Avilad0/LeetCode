class TrieNode:
    def __init__(self):
        self.trieMap = {}
        self.isWordEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.trieMap:
                curr.trieMap[c] = TrieNode()            
            curr = curr.trieMap[c]
        
        curr.isWordEnd = True

    def search(self, word: str) -> bool:
        n=len(word)

        def searchInTrie(trieNode, i):
            if i==n:
                return trieNode.isWordEnd
                
            if word[i] == ".":
                for (k,v) in trieNode.trieMap.items():
                    if searchInTrie(v, i+1):
                        return True
                
                return False

            if word[i] not in trieNode.trieMap:
                return False

            return searchInTrie(trieNode.trieMap[word[i]], i+1)
        
        return searchInTrie(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)