# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []

        node = head
        while node:
            array.append(node.val)
            node = node.next

        array = sorted(array)

        dummyNode = ListNode(None)
        node = dummyNode

        for x in array:
            nextNode = ListNode(x)
            node.next = nextNode
            node = nextNode
        
        return dummyNode.next