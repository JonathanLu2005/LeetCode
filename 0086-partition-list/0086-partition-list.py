# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = []
        second = []

        node = head
        while node:
            if node.val < x:
                first.append(node.val)
            else:
                second.append(node.val)
            node = node.next

        n = len(first) + len(second)

        node = head
        i = 0
        array = first + second

        node = head
        while node:
            node.val = array[i]
            i += 1
            node = node.next
        return head
