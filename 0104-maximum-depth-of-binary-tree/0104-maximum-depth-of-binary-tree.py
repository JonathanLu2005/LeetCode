# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative DFS, emulate callstack for DFS
        # done with left subtree, pop back to middle, then go right subtree
        # do preorder for iteratively, process middle, add children to stack
        # then left then right
        # for each node add the depth

        if not root:
            return 0

        # stack w root and depth of 1
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()

            # prevent null node
            if node:
                # res is max of depth or res
                res = max(res, depth)
                # go left and right and increase depth
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


        """
        # BFS is level order, uses a queue
        # have root , level 1
        # go to root, dequeue it, then eqneue its children to queue
        # 2nd level, left first, right last
        # then repeat
        # then keep going and return max level

        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:
            # traverse level and pop
            for i in range(len(q)):
                node = q.popleft()
                # aka when visit node, append it childre
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # does BFS of going trhough quqe, add children, then go through again
            level += 1
        return level
        # when empty return levels
"""
        """
        # DFS or BFS

        # DFS recursive
        # go to each subtree, then return the max height
        # then at end + 1, so 1 + max(left, right)
        # so thats how we get the int, no val needed, do this
        # as already traverse so only worry abt value
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


"""





        # go traverse every node in in order
        # keep a count
        # once the node is none
        # change the val to the max of the val and the count
        # then when going back start taking away 1



"""
        big = 0
        big = max(big, inOrder(root, 0))

        return big

def inOrder(root, val):
    if not root:
        return val

    inOrder(root.left, val + 1)
    inOrder(root.right, val + 1)

    return val
        """