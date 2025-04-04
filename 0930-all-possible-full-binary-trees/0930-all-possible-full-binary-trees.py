# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # could make the generic tree then alter it
        # first node is mandatory, so we've n-1 nodes
        # then we need children for first node so we've n -1 -2 nodes
        # then split between like 2x between either side
        # look at a pattern to save time from brute force
        # then it becomes sub problems when we split between 2x on either side
        # figure out how many trees we can make

        # optimise cache, store basecases
        dp = { 0: [], 1: [TreeNode()]}

        # return list of full binary trees with n nodes
        def backtrack(n):
            # if computed return
            if n in dp:
                return dp[n]

            result = []

            for l in range(n):
                # calculate right
                r = n - 1 - l

                # find trees for left and right
                leftTrees, rightTrees = backtrack(l), backtrack(r)

                # calculate differentr trees from either side
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        # create tree with lef tand right subtree
                        result.append(TreeNode(0, t1, t2))
            dp[n] = result
            return result
        
        return backtrack(n)