# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        node = head
        numbers = []

        while node:
            if node.val is None:
                break
            numbers.append(node.val)
            node = node.next

        # formula to convert soted list to bst
        def createBST(array):
            if not array:
                return None

            middle = len(array) // 2
            root = TreeNode(array[middle])

            root.left = createBST(array[:middle])
            root.right = createBST(array[middle+1:])

            return root

        return createBST(numbers)