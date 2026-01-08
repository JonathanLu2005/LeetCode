# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #GT = every key in BST
        # is key + sum of key grather than original key
        
        # OH, so we get all the values
        # then we add them to original key
        # could just get all values, then traverse each value and update htem one by one, so 2n
        keys = []

        def dfs1(node):
            nonlocal keys
            if not node.left and not node.right:
                return node.val

            if node.left:
                left = dfs1(node.left)
                keys.append(left)
            if node.right:
                right = dfs1(node.right)
                keys.append(right)
            return node.val
        dfs1(root)
        keys.append(root.val)

        def dfs2(node):
            nonlocal keys
            if not node.left and not node.right:
                key = sum([x for x in keys if x >= node.val])
                node.val = key
                return

            if node.left:
                left = dfs2(node.left)
            if node.right:
                right = dfs2(node.right)
            key = sum([x for x in keys if x >= node.val])
            node.val = key
            return
        dfs2(root)

        return root
        