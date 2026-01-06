# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # root level is 1, next 2, so forth
        # find the level x s.t. the sum of all values of node at said level, is max
        # oh find level with biggest sum
        # can do BFS, go through each layer, calculate their values
        # and then store whatever has the highest score and what level they're in to compare and return the result
        if not root.left and not root.right:
            return 1
        
        highest = float("inf") * -1
        result = 0
        level = 0
        queue = deque([root])

        while queue:
            total = 0
            level += 1

            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                total += node.val

            if total > highest:
                highest = total
                result = level

        return result
            
