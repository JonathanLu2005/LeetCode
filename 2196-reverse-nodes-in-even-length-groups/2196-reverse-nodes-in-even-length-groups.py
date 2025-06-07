# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse, s.t. we get 1, 2, 3, as windows, and reverse even ones
        target = 1
        ctr = 0

        current = []
        final = []

        node = head

        while node:
            current.append(node.val)
            node = node.next
            ctr += 1

            if ctr == target:
                if target % 2 == 0:
                    current = current[::-1]
                final.extend(current)
                target += 1
                ctr = 0
                current = []

        if ctr % 2 == 0:
            current = current[::-1]
        final.extend(current)

        dummy = ListNode(0)
        node = dummy

        for x in final:
            newNode = ListNode(x)
            node.next = newNode
            node = newNode
        
        head = dummy.next
        return head