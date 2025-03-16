# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node -> node -> node
        # if we see the next node is same
        # we need a train of 2 node
        # where
        # A -> B -> B
        # 2nd see has dupe, then itll delete upfront till no more
        # then one behind can change next to one ahead of it
        # A -> B -> C , change so A -> C
        # then if all good, move up, and keep going till its none
        # only issue what if start is dupe, then we need a dummy node first
        # O(n)
        if not head or not head.next:
            return head

        # then return dummy node nexgt
        dummyNode = ListNode()
        dummyNode.next = head

        firstNode = dummyNode
        secondNode = firstNode.next

        while secondNode and secondNode.next:
            if secondNode.val == secondNode.next.val:
                while secondNode.next and secondNode.val == secondNode.next.val:
                    secondNode.next = secondNode.next.next
                firstNode.next = secondNode.next
                secondNode = firstNode.next
            else:
                firstNode = secondNode
                secondNode = secondNode.next

        return dummyNode.next
