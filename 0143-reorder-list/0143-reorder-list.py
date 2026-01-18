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
        # so its first last, second first second last ...
        # get the value into array
        # then 2 pointers it
        # then convert into linked list
        array = []

        node = head

        while node:
            array.append(node.val)
            node = node.next

        result = []

        p1 = 0
        p2 = len(array) - 1

        while p1 <= p2:
            if p1 != p2:
                result.append(array[p1])
                result.append(array[p2])
            else:
                result.append(array[p1])
            p1 += 1
            p2 -= 1


        i = 0
        node = head
        while node:
            node.val = result[i]
            i += 1
            node = node.next

