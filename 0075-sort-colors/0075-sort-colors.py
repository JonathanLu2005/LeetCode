class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get count of each, then as we loop throguh nums change it and shi
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)
        index = 0

        while index < len(nums):
            while zero != 0:
                nums[index] = 0
                index += 1
                zero -= 1
            while one != 0:
                nums[index] = 1
                index += 1
                one -= 1 
            while two != 0: 
                nums[index] = 2
                index += 1 
                two -= 1
        
        