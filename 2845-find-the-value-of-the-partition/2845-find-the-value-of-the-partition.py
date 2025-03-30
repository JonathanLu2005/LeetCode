class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        # partition into num1 num2
        # both array are non empty
        # value of partition is minimised
        # want it such that we've 2 very close numbers
        # because we can sort it and partition it however
        # could just try find nicest difference
        # might be best to sort it
        nums = sorted(nums)
        result = float("inf")

        for x, y in zip(nums, nums[1:]):
            result = min(result, abs(x-y))
        return result