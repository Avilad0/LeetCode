class TrieNode:
    def __init__(self):
        self.isWordEnd = False
        self.trieMap = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.trieMap:
                curr.trieMap[word[i]] = TrieNode()
            
            curr = curr.trieMap[word[i]]
        
        curr.isWordEnd = True


    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.trieMap:
                return False
            
            curr = curr.trieMap[word[i]]
        
        return curr.isWordEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.trieMap:
                return False
            
            curr = curr.trieMap[prefix[i]]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)