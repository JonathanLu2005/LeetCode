class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking, have 2 choices, we either add, or we dont
        # keep track of index and decide if we want to add or not add
        result = []
        n = len(nums)

        def backtrack(index,subset):
            if index == n:
                result.append(subset.copy())
                return

            subset.append(nums[index])
            index += 1
            backtrack(index, subset)

            subset.pop(-1)
            backtrack(index, subset)

        backtrack(0,[])
        return result