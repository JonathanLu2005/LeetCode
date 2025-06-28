# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # preorder traversal
        # node = int val, if has children should be in parentheses
        # empty parentheses for no child
        # remove them unless its no left and 1 right, then keep
        # just do DFS, then every time we explore, add left bracket, add value, continue, then add right bracket after done

        def dfs(node):
            if not node:
                return ""
            if node.left and node.right:
                return str(node.val) + "(" + dfs(node.left) + ")(" + dfs(node.right) + ")" 
            elif node.left:
                return str(node.val) + "(" + dfs(node.left) + ")" 
            elif node.right:
                return str(node.val) + "()" + "(" + dfs(node.right) + ")" 
            else:
                return str(node.val) 
        return dfs(root)