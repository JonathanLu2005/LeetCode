# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        values = []

        node = head
        while node:
            values.append(node.val)
            node = node.next

        values = sorted(values)
        dummyNode = ListNode()
        node = dummyNode

        for x in values:
            newNode = ListNode(x)
            node.next = newNode
            node = newNode

        return dummyNode.next