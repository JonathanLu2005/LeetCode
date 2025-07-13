# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # just get entire thing, then reverse from left to right
        # then continue, then amek into linked list
        array = []
        reverse = []

        node = head
        count = 1
        while node is not None:
            if count >= left and count <= right:
                reverse.append(node.val)

                if count == right:
                    reverse = reverse[::-1]
                    array.extend(reverse)
            else:
                array.append(node.val)
            count += 1
            node = node.next

        dummyNode = ListNode()
        node = dummyNode

        for x in array:
            nextNode = ListNode(x)
            node.next = nextNode
            node = nextNode

        return dummyNode.next
