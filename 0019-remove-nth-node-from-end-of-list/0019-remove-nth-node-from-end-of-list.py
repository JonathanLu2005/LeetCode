# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = 0

        node = head
        while node:
            t += 1
            node = node.next

        if t == 1 and n == 1:
            return None

        t -= (n+1)

        if t < 0:
            return head.next
        
        node = head
        while t > 0:
            t -= 1
            node = node.next
        
        if node.next.next:
            node.next = node.next.next
        else:
            node.next = None
        return head
