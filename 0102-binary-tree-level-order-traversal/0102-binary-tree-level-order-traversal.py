# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS level by level
    # then put all the nodes into array and put into a grand arrray
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # do BFS
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res

        """
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            # so instead of level holding number of depth
            # it hold values till qlen is empty as no more to go through
            # then after getting vals for that level, adds it to the array
            for i in range(qLen):
                node = q.popleft()
                if node:
                    # alter it as now store value for levels
                    level.append(node.val)
                    # q for usual bfs
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
        """


"""
        if not root:
            return [] 
        
        finalArr = []
        q = deque([root])

        while q:
            arr = []
            for i in range(len(q)):
                node = q.popleft()
                arr.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            finalArr.append(arr)
        return finalArr
"""