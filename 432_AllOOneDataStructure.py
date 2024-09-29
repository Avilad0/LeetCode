class Node:
    def __init__(self, freq:int):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.freqMap = {}
    
    def inc(self, key: str) -> None:
        
        if key in self.freqMap:
            node = self.freqMap[key].next
            if node==self.tail:
                node = Node(self.freqMap[key].freq+1)
                self.freqMap[key].next=node
                self.tail.prev=node
                node.next=self.tail
                node.prev = self.freqMap[key]
            
            node.keys.add(key)
            self.freqMap[key].keys.remove(key)
            self.freqMap[key] = node

        else :
            if 

    def dec(self, key: str) -> None:

    def getMaxKey(self) -> str:

    def getMinKey(self) -> str:
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()




'''
Input
["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"]
[[],["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]

Use Testcase
Output
[null,null,null,null,null,"hello",null,null,null,null,null,null,null,"hello"]
Expected
[null,null,null,null,null,"hello",null,null,null,null,null,null,null,"leet"]
'''