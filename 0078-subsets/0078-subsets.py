class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # keep track of index and choose to keep index or not
        result = []
        n = len(nums)
        subset = []

        def backtrack(index):
            if index == n:
                result.append(subset[:])
                return

            subset.append(nums[index])
            backtrack(index+1)

            subset.pop(-1)
            backtrack(index+1)
        backtrack(0)
        return result

