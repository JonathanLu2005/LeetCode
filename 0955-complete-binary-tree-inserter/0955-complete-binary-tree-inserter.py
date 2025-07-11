# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def insert(self, val: int) -> int:
        q = collections.deque()
        q.append(self.root)

        while q:
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()

                if node:
                    if not node.left:
                        node.left = TreeNode(val)
                        return node.val
                    else:
                        q.append(node.left)
                    if not node.right:
                        node.right = TreeNode(val)
                        return node.val
                    else:
                        q.append(node.right)



    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()