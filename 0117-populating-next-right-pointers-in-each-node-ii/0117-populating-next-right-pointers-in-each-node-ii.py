"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = collections.deque()
        q.append(root)

        while q:
            lenQ = len(q)
            level = []

            for i in range(lenQ):
                node = q.popleft()

                if node:
                    level.append(node)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                for i in range(0, len(level) - 1):
                    level[i].next = level[i+1]
        return root
