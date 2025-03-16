# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recursive DFS is slow, instead of askig balance at root node
        # ask at each sbutree from bottom up
        # before O(n^2)
        # should ask if balance at each
        # determine if balance at each node, so bottom up
        # so idea go up then get O(n)
        # return T/F if balance then reutrn height

        def dfs(root):
            # empty tree, is true, and 0 height
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            # height in index 1, abs saves the max() - max() stuff
            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)
            # balanced tells if true balance, false not balance, and new height
            # so find height and find out if balance
            return [balanced, 1+max(left[1], right[1])]

        return dfs(root)[0]
        """
        global current
        current = True


        def dfs(root):
            global current
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            print(root.val)
            print(left)
            print(right)
            print("moving to next")

            if max(left,right) - min(left,right) > 1:
                print("DOES THIS EVER GET CALLED?")
                current = False

            return max(left,right) + 1

        dfs(root)

        return current"""