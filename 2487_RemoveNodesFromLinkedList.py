from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        if head==None or head.next==None:
            return head
        
        nextNode = self.removeNodes(head.next)

        if nextNode.val > head.val:
            return nextNode
        
        head.next = nextNode
        return head


        # TLE in large descending values due o(n*n) in case of descending list
        # if head==None or head.next==None:
        #     return head
    
        # m = head.val
        # m_node=head
        # node = head.next
        # while node:
        #     while node.next and node.val<m:
        #         node = node.next
            
        #     if node.val==m:
        #         m_node.next = node
        #         m_node = node
        #         node=node.next
        #     elif node.val>m:
        #         head = node
        #         m = node.val
        #         m_node = node
        #         node=node.next
        #     else:
        #         break
            
        # m_node.next = self.removeNodes(m_node.next)

        # return head



print(Solution().removeNodes(ListNode(5,ListNode(2, ListNode(13, ListNode(3,ListNode(8)))))))
print(Solution().removeNodes(ListNode(1,ListNode(1, ListNode(1, ListNode(1,ListNode(1)))))))


#   5,      2,  13,     3,  8
#  h,s,f
#   h,s         f
#               h,s,f
#               h,s         f
#               


#   1,      1,      1,     1,       1
#  h,s,f
#   h,s                             f
#               h,s,f
#               h,s         f
#               



# 2,        2,      1,      2,          2,      0
# 