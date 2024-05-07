from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head

        if node.val>4:
            head = ListNode(1,node)

        while node.next:
            # node.val = (node.val*2 + ((node.next.val*2)//10))%10
            node.val = (node.val*2 + (node.next.val>4))%10

            node=node.next

        node.val = (node.val*2)%10

        return head

        # n = 0
        # node=head
        # while node:
        #     n=n*10 + node.val
        #     node=node.next


        # n=str(n*2)
        # i=0
        # node=head
        # while node.next:
        #     node.val=int(n[i])
        #     node=node.next
        #     i+=1
        
        # node.val = int(n[i])
        # i+=1
        # if i!=len(n):
        #     node.next = ListNode(n[i])
            
                
        # return head