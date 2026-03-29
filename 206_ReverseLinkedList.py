from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative Soltion. tc= O(n), sc=O(1)    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        newHead = None
        while node:
            temp = node.next
            node.next = newHead
            newHead = node
            node = temp
        
        return newHead


l =ListNode(1,ListNode(2,None))
    
l = Solution().reverseList(l)


while l!=None:
    print(l.val)
    l = l.next


# # Alternative recursive Soltion. tc= O(n), sc=O(n)
# class Solution:

#     def recur(self, node: Optional[ListNode]) -> Optional[ListNode]:
#         if node==None:
#             return None
        
#         newParent = self.recur(node.next)
#         if newParent==None:
#             self.newHead = node
#         else:
#             newParent.next=node
#         return node

#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
            
#         self.recur(head)
#         head.next=None
#         return self.newHead
