# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # return each level
        if not root:
            return []
        queue = deque([root])
        result = []

        while queue:
            layer = []

            for i in range(len(queue)):
                node = queue.popleft()
                layer.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(layer)
        return result

