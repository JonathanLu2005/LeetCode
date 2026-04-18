# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # put them into string, then convert intointeger, then add, then convret into string to iterate, then convret into integer
        # and create thingy
        l1value = ""
        l2value = ""

        node = l1
        while node:
            l1value += str(node.val)
            node = node.next

        node = l2
        while node:
            l2value += str(node.val)
            node = node.next

        value = str(int(l1value[::-1]) + int(l2value[::-1]))[::-1]

        head = ListNode()
        node = head

        for x in value:
            newNode = ListNode()
            newNode.val = int(x)
            node.next = newNode
            node = newNode

        return head.next

