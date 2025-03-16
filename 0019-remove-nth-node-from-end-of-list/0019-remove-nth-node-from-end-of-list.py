# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy 
        right = head

        # create dummy as left and right keep moving till n=0
        while n > 0 and right:
            right = right.next
            n -= 1

        # then keep shifting till right is empty
        while right:
            left = left.next 
            right = right.next 

        # change left pointer to get rid of the node, able return list
        # idea is shifting
        left.next = left.next.next 
        return dummy.next
        
        """
        if head is None:
            return None

        l = 1  
        curr = head 

        while curr.next != None:
            curr = curr.next
            l += 1

        curr = head
        c = 1

        while c != (l-n-1):
            curr = curr.next 
            c += 1

        curr.next = curr.next.next

        return head
        """