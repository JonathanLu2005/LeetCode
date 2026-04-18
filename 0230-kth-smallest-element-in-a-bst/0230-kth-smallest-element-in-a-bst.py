# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # find all nodes then return k
        queue = deque([root])
        values = []

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        values = sorted(values)

        return values[k-1]