# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # reverse the nodes from left to right
        # uhh so get all the nodes
        # and we add them in right order to another node
        # but moment we hit left, then we add it into a stack
        # until we finish going to right
        # and once we do that, reverse that,and extend it to the main result
        # and keep going on further
        values = []

        node = head
        while node:
            values.append(node.val)
            node = node.next

        result = []
        stack = []

        for i in range(len(values)):
            if (i+1) >= left and (i+1) <= right:
                stack.append(values[i])
            else:
                result.append(values[i])

            if (i+1) == right:
                stack = stack[::-1]
                result.extend(stack)

        dummyNode = ListNode()
        node = dummyNode

        for x in result:
            newNode = ListNode(x)
            node.next = newNode
            node = newNode
        
        return dummyNode.next
