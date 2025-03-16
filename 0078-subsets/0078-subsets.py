class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res








        """
        # like decision tree, add 1 and not add 1
        # then add 2 or not add 2, so on with 3
        # then have subset and decide if want to add 3 or not,
        # just repeat decision and be like want to add this or not
        # like deciison tree with many different altneratives
        # get all results

        #result list
        res = []

        # array to hold reslt 
        subset = []
        # use dfs, i is index of value making decision on
        def dfs(i):
            # bc if out of bound
            if i >= len(nums):
                # add copy, then subset will be modified later
                res.append(subset.copy())
                return 

            # decision to include
            subset.append(nums[i])
            # then make deicsion on next el
            dfs(i + 1)

            # decision not to
            subset.pop()
            dfs(i + 1)
            # then keep going to see if want 

        dfs(0)
        return res
        """
