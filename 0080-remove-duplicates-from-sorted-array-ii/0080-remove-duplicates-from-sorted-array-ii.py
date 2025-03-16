class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leftPtr = 0
        rightPtr = 1

        while rightPtr != len(nums):
            val1 = nums[leftPtr] 
            val2 = nums[rightPtr]

            rightPtr += 1
            leftPtr += 1

            if val1 == val2:
                while rightPtr != len(nums) and val1 == nums[rightPtr]:
                    nums.pop(rightPtr)

        return len(nums)
