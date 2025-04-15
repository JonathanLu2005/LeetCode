# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # moment we find a none, everything else must be a none!

        queue = deque([root])
        noneFound = False

        while queue:
            node = queue.popleft()

            if noneFound:
                if node is not None:
                    return False
            else:
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    noneFound = True
        return True
                