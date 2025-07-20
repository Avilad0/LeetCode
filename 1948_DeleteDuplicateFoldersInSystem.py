from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self, currFolderName):
        self.currFolderName = currFolderName
        self.subFolderStructure = ""
        self.children = {}


class Solution:    
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode('/')

        for p in paths:
            curr = root
            for f in p:
                if f not in curr.children:
                    curr.children[f] = TrieNode(f)
                curr = curr.children[f]
        
        
        freqOfUniqueChildStructure = defaultdict(int)

        def dfs(curr: TrieNode):
            if len(curr.children)==0:
                return
            
            folderStructure = []
            for child, childNode in curr.children.items():
                dfs(childNode)
                folderStructure.append(child +"[" + childNode.subFolderStructure + "]")
            
            folderStructure.sort()
            curr.subFolderStructure = "".join(folderStructure)
            freqOfUniqueChildStructure[curr.subFolderStructure] +=1
            
        
        dfs(root)

        ans = []
        currPath = []
        def checkForDuplicates(curr:TrieNode):
            if freqOfUniqueChildStructure[curr.subFolderStructure]>1:
                return
            
            if currPath:
                ans.append(currPath[:])
            
            for child, childNode in curr.children.items():
                currPath.append(child)
                checkForDuplicates(childNode)
                currPath.pop()    
        
        checkForDuplicates(root)

        return ans