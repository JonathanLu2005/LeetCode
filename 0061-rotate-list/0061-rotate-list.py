# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # will want to mod it by length 
        # get to last node
        # then do entire length - thingy
        # then keep going through first one, add it to end
        # and keep going until done
        if not head or not head.next:
            return head

        length = 1
        lastPtr = head

        while lastPtr.next:
            length += 1
            lastPtr = lastPtr.next

        # get last pointer
        k = k % length
        k = length - k

        frontier = head
        while k != 0:
            prevFrontier = frontier
            frontier = frontier.next

            lastPtr.next = prevFrontier
            lastPtr = lastPtr.next
            lastPtr.next = None
            k -= 1
        return frontier
