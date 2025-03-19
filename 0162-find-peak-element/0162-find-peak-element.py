class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            return 1

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        
        maxNumber = max(nums)
        return nums.index(maxNumber)