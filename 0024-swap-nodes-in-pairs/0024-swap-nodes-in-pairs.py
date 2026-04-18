# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        second = []
        first = []
        swap = False

        node = head
        k = 0
        while node:
            k += 1
            if not swap:
                second.append(node.val)
                swap = True
            elif swap:
                first.append(node.val)
                swap = False

            node = node.next

        if k <= 1:
            return head

        dummyNode = ListNode()
        node = dummyNode
        swap = False

        while k > 0:
            if (not swap and first) or (k == 1 and first):
                x = first.pop(0)
                swap = True
            elif (swap and second) or (k == 1 and second):
                x = second.pop(0)
                swap = False

            newNode = ListNode(x)
            node.next = newNode
            node = newNode
            k -= 1

        return dummyNode.next