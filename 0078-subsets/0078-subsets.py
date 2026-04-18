class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking, 2 choices, keep or not keep, and continue on

        result = []

        def backtracking(index, subset):
            if index == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[index])
            index += 1
            backtracking(index,subset)

            subset.pop(-1)
            backtracking(index,subset)

        backtracking(0,[])
        return result