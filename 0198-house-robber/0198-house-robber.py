class Solution:
    def rob(self, nums: List[int]) -> int:
        # whats mroe, robbing the house before and ignoring urs, or robging this house and the one beefore that
        # either 
        n = len(nums)

        if n >= 2:
            nums[1] = max(nums[0], nums[1])

        for i in range(2,n):
            result = max(nums[i-1], nums[i] + nums[i-2])
            nums[i] = result
        return max(nums)
