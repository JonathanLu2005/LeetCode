# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # traverse and get the left and right depth
        # then compare, if equal, return the current node
        # else return node of deepest
        def dfs(node, depth):
            if not node:
                return None, depth

            depth += 1
            nl, dl = dfs(node.left,depth)
            nr, dr = dfs(node.right,depth)

            if dl == dr:
                return node, dl
            elif dl > dr:
                return nl, dl
            return nr, dr
        rn, rd = dfs(root,1)
        return rn


        """
        # keep going down to find the largest depth
        # and if it has the biggest depth
        # the parent node will return its node and what level
        # idea is that let say we go to 2, realise it has largest
        # then we'll store level 3 = 2, then level 2 = 5, level 1 = 3
        # and aim for the lowest level first
        # however if 0 had the deepest leavestoo, this mean we'll have
        # level 3 = 2, 0,level 2 = 5,1, level 0 = 3
        # so we'll want the level thats the lowest and only has 1 node in it
        # and we'll return that node
        # if we get a new contendor, e.g a bigger depth, then we'll just erase the hashmap lol
        # dfs it
        maxDepth = 0
        hashmap = {}

        def dfs(node, level, depth):
            nonlocal maxDepth
            nonlocal hashmap
            if not node:
                return level, depth

            depth += 1
            level += 1

            leftlvl, leftdep = dfs(node.left, level, depth)
            rightlvl, rightdep = dfs(node.right, level, depth)

            currentDepth = max(rightdep, leftdep)

            if currentDepth > maxDepth:
                maxDepth = currentDepth 
                hashmap = {}

            if currentDepth == maxDepth:
                if level not in hashmap:
                    hashmap[level] = []
                hashmap[level].append(node)
            level -= 1

            return level, depth
        dfs(root,0,1)
        maxLevel = max(hashmap.keys())

        print(hashmap)

        for key in range(maxLevel, -1, -1):
            if key in hashmap:
                if len(hashmap[key]) == 1:
                    return hashmap[key][0]
        return
        """