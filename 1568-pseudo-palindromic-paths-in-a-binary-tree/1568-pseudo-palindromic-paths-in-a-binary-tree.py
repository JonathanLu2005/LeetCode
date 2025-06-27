# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # dfs to find every path
        # keep hashmap, of frequencies, then once hit a deadend, aka no children
        # see if its plaindrome if it has multiple odd frequencies
        
        def dfs(node, hashmap):
            if not node:
                return 0

            hashmap[node.val] = hashmap.get(node.val,0) + 1

            if not node.left and not node.right:
                count = sum(1 for x in hashmap.values() if x % 2 == 1)

                if count <= 1:
                    result = 1
                else:
                    result = 0
            else:
                result = dfs(node.left, hashmap) + dfs(node.right, hashmap)

            hashmap[node.val] -= 1
            return result

        return dfs(root,{})
