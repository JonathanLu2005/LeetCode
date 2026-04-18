# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # first last second second last
        # so get everything
        # then 2 pointer it to craete new list
        # then make new linked list
        values = []

        node = head
        while node:
            values.append(node.val)
            node = node.next

        p1 = 0
        p2 = len(values) - 1

        result = []

        while p1 <= p2:
            if p1 == p2:
                result.append(values[p1])
            else:
                result.append(values[p1])
                result.append(values[p2])

            p1 += 1
            p2 -= 1

        node = head

        for x in result:
            node.val = x
            node = node.next

 

