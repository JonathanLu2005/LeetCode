# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None 

        res = []

        def DFS(root, substring):
            substring += str(root.val)

            if not root.left and not root.right:
                res.append(substring)
                return 

            if root.left:
                DFS(root.left, substring)
            if root.right:
                DFS(root.right, substring)

        DFS(root, "")
        res = [int(x) for x in res]
        return sum(res)