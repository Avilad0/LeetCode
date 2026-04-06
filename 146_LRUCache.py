# Same approach as Below but using dummy start and end node to prevent extra checking on the edge conditions 
# tc: O(1), 
class ListNode:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.start = ListNode("start")
        self.end = ListNode("End", self.start)
        self.start.nxt = self.end

    def removeNode(self, node):
        
        prevNode, nxtNode  = node.prev, node.nxt
        prevNode.nxt, nxtNode.prev = nxtNode, prevNode
        
        self.capacity+=1
        

    def insertAtEnd(self, node):
        prevNode, nxtNode = self.end.prev, self.end

        prevNode.nxt, nxtNode.prev = node, node
        node.nxt, node.prev = nxtNode, prevNode

        self.capacity-=1

    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        (val, node) = self.cache[key]

        self.removeNode(node)
        self.insertAtEnd(node)

        return val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            (_ , node) = self.cache[key]
            self.removeNode(node)

        if self.capacity==0:
            del self.cache[self.start.nxt.val]
            self.removeNode(self.start.nxt)


        node = ListNode(key)
        self.insertAtEnd(node)

        self.cache[key] = (value, node)



# class ListNode:
#     def __init__(self, val, prev=None, nxt=None):
#         self.val = val
#         self.prev = prev
#         self.nxt = nxt

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.capacity = capacity
#         self.currCapacity = 0
#         self.start = None
#         self.end = None

#     def moveToEnd(self, node):
#         if node!=self.end:
#             prevNode = node.prev
#             nxtNode = node.nxt
#             node.prev = node.nxt = None

#             if node==self.start:
#                 nxtNode.prev = None
#                 self.start=nxtNode
#             else:
#                 prevNode.nxt = nxtNode
#                 nxtNode.prev = prevNode

#             self.end.nxt=node
#             node.prev = self.end
#             self.end = node
        

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
        
#         (val, node) = self.cache[key]

#         self.moveToEnd(node)

#         return val

#     def put(self, key: int, value: int) -> None:

#         if key in self.cache:
#             (_ , node) = self.cache[key]
#             self.moveToEnd(node)
#             self.cache[key] = (value, node)
#             return

#         if self.currCapacity>=self.capacity:
#             del self.cache[self.start.val]
#             nodeToDel = self.start

#             if self.start==self.end:
#                 self.start=self.end=None
#             else:
#                 self.start = self.start.nxt
#                 self.start.prev = None
            
#             del nodeToDel
#             self.currCapacity-=1


#         node = ListNode(key)
#         self.cache[key] = (value, node)
#         if self.start==None:
#             self.start=self.end=node
#         else:
#             self.end.nxt = node
#             node.prev = self.end
#             self.end = node

#         self.currCapacity+=1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)