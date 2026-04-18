# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs, on evrey layer, we onlycare about the far right
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            value = 0
            for i in range(len(queue)):
                node = queue.popleft()
                value = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(value)
        return result

        