# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # root to leaf path wher sum = target sum
        # dfs, as we traverse, we keep incrementing, and moment we hit the elaf node, we check if equal target sum
        # if so we increment result
        # otherwise we go back and we need to decrement our value as we go back
        result = []

        def dfs(node,value,path):
            nonlocal result
            if not node:
                return

            value += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if value == targetSum:
                    result.append(path.copy())
            else:
                dfs(node.left,value,path)
                dfs(node.right,value,path)

            path.pop(-1)

        dfs(root,0,[])
        return result
