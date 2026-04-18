# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # ahh so given the whoel thing, we want to move it right
        # first we want to mod k by the length of list
        # as that'll be the ultimate changes
        # and then we can just swap every gu from right to start
        if not head:
            return None

        values = []
        n = 0

        node = head
        while node:
            values.append(node.val)
            node = node.next
            n += 1

        k = k % n

        while k > 0:
            v = values.pop(-1)
            values.insert(0,v)
            k -= 1

        dummyNode = ListNode()
        node = dummyNode
        for x in values:
            newNode = ListNode(x)
            node.next = newNode
            node = newNode
        return dummyNode.next


        