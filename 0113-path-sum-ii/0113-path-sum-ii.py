# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def DFS(subset, root):
            subset.append(root.val)

            if not root.left and not root.right:
                print(subset)
                if sum(subset) == targetSum:
                    res.append(subset.copy())

            if root.left:
                DFS(subset, root.left)
            if root.right:
                DFS(subset, root.right)

            subset.pop(len(subset)-1)
            return

        if root:
            DFS([], root)

        return res
            