# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # reverse every 2nd
        if not root:
            return []
        count = 1
        result = []

        queue = deque([root])
        while queue:
            layer = []
            for i in range(len(queue)):
                node = queue.popleft()
                layer.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if count % 2 == 0:
                layer = layer[::-1]
            result.append(layer)
            count += 1

        return result
