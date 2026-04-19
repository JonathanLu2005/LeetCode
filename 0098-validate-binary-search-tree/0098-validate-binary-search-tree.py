# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # ahhh so on left must be decreasing, on right must be increasing
        # moment left is more than parent, return false
        # else keep going till all good then return true
        # and whtaever we get return we should add that to final value and see what fina lvalue says
        # oh yeah if bad, we can pass the value false, andjust and it, then we just return the value

        def dfs(node, minVal, maxVal):
            if not node:
                return True
            
            if not (minVal < node.val < maxVal):
                return False

            return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)
        
        return dfs(root, float("-inf"), float("inf"))
            

            
