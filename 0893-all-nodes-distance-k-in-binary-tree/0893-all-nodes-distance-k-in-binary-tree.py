# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # make it undirected graph
        # then bfs from target where ditsncae is 2
        if k == 0:
            return [target.val]

        hashmap = {}

        stack = [[root, None]]

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
        
        queue = [target.val]
        visited = set()
        count = 0

        while queue:
            newQueue = []

            for node in queue:
                if node in visited:
                    continue
                visited.add(node)

                if node in hashmap:
                    newQueue.extend(hashmap[node] - visited)
            queue = newQueue
            count += 1

            if count == k:
                return queue
        return []