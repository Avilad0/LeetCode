from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# tc=O(n), sc=O(1), 
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        old = head
        while old:
            new = Node(old.val, old.next, old.random)
            old.next = new
            old=new.next
        
        old = head
        while old:
            new =old.next
            if new.random:
                new.random = new.random.next
            old=new.next
        
        newHead = Node(0)
        old, new =head, newHead
        while old:
            new.next = old.next
            new=new.next
            old.next=old.next.next
            old=old.next

        return newHead.next

'''
1st pass
for list A>B>C
create new Nodes as next nodes: A>A'>B>B'>C>C'
with A'.random = A.random

2nd pass
replace A'.random = A.random.next = (as next is newly created node for A.random)

3rd pass
separate 2 list: A>B>C and A'>B'>C'

'''

# # tc=O(n), sc=O(n), using hashmap - same as below
# class Solution:
#     def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

#         oldToNew = {None:None}

#         old = head
#         while old:
#             oldToNew[old] = oldToNew.get(old, Node(old.val))
#             if old.next!=None:
#                 oldToNew[old].next = oldToNew[old.next] = oldToNew.get(old.next, Node(old.next.val))
#             if old.random!=None:
#                 oldToNew[old].random = oldToNew[old.random] = oldToNew.get(old.random, Node(old.random.val))
#             old=old.next
            
#         return oldToNew[head]
    

# # tc=O(n), sc=O(n), using hashmap - same as above
# class Solution:
#     def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
#         if not head:
#             return None
#         oldToNew = { head: Node(head.val)}

#         old, new = head, oldToNew[head]
#         while old:
#             if old.next:
#                 if old.next not in oldToNew:
#                     oldToNew[old.next]= Node(old.next.val)
#                 new.next = oldToNew[old.next]

#             if old.random:
#                 if old.random not in oldToNew:
#                     oldToNew[old.random]= Node(old.random.val)
#                 new.random = oldToNew[old.random]

#             old, new = old.next, new.next
        
#         return oldToNew[head]