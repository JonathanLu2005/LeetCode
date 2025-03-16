# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
DFS

"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # go through each node, if its not node return true as all good
        def dfs(node, minVal, maxVal):
            if not node:
                return True
            
            # if violate return false
            if not (minVal < node.val < maxVal):
                return False

            # both needs to be true
            # going up so node.val and whatnot is their elft or right
            return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)
        
        return dfs(root, float("-inf"), float("inf"))
                
        
        

        