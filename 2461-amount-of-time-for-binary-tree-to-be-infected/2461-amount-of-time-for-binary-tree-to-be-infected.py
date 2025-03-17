# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # conver tto undriected graph
        # 1: 5 3
        # 3: 10 6 1
        # 5: 4 1
        # 4: 9 2
        # 9: 4
        # 2: 4
        # 10: 3
        # 6: 3
        # keep count how many iterations we need till we cover everything

        # undirected graph
        stack = [[root, None]]
        hashmap = {}

        while stack:
            node, parent = stack.pop()

            if node:
                leftChild = node.left
                rightChild = node.right

                value = set()
                if leftChild:
                    value.add(leftChild.val)
                if rightChild:
                    value.add(rightChild.val)
                if parent:
                    value.add(parent.val)
                hashmap[node.val] = value

                stack.append([leftChild, node])
                stack.append([rightChild, node])
        
        # bfs
        visited = set()
        queue = [start]
        time = -1

        while queue:
            newQueue = []
            for node in queue:
                if node in visited:
                    continue
                visited.add(node)

                if node in hashmap:
                    newQueue.extend(hashmap[node] - visited)
            queue = newQueue
            time += 1
        return time
