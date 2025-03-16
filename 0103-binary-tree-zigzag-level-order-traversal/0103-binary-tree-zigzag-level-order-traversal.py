# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        res = []
        c = 0

        while q:
            c += 1
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()

                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
                
            if c % 2 == 0:
                level = level[::-1]

            res.append(level)

        res.pop()
        return res

