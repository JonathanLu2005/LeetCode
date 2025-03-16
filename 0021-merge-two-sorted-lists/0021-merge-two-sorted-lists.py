# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        # just keep switching between, dummy node is elite
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # then last can just put entire list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

        """
        l1Head = list1 
        l2Head = list2
    
        while l1Head.next is not None and l2Head.next is not None:
            if l1Head.val == l2Head.val:
                tail.next = l1Head 
                tail = tail.next
                l1Head = l1Head.next 
            else:
                tail.next = l2Head
                tail = tail.next 
                l2Head = l2Head.next 
        while l2Head.next is not None:
            tail.next = l2Head
            tail = tail.next
            l2Head = l2Head.next

        return dummy.next
        """