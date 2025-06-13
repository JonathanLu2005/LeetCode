# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        # as add to stack, if value smaller than current value, then its left child of current value
        # otherwise whatevers recently aded to stack, next value is the right child
        # append tree node so can return index 0
        stack = []

        for x in nums:
            node = TreeNode(x)

            while stack and stack[-1].val < x:
                node.left = stack.pop()

            if stack:
                stack[-1].right = node

            stack.append(node)
        return stack[0]