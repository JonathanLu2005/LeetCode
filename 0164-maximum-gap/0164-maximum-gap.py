class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # return max diff between 2 element in sorted form
        # if have less than 2 element, return 0
        # oh its legit going by point by point
        n = len(nums)
        if n < 2:
            return 0
        nums = sorted(nums)
        result = 0

        for i in range(0,n-1):
            result = max(result,nums[i+1]-nums[i])
        return result