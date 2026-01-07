# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # result is max ( ( total - subtree ) * subtree)
        # so we first get the total
        # then we get each subtree and keep the max
        # oh with dfs, wecan check left and rgiht child
        # else we add up
        result = -1 * float("inf")
        total = 0

        def dfs(node):
            nonlocal result, total
            if not node:
                return 0

            temp = node.val + dfs(node.left) + dfs(node.right)
            result = max(result, (total-temp) * temp)
            return temp
        total = dfs(root)
        dfs(root)
        return result % (10**9+7)