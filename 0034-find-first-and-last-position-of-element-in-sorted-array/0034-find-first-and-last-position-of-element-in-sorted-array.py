class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # do binary search, then two pointers explring further to figure out where it starts and end

    

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                leftPtr = middle

                while leftPtr > -1 and nums[leftPtr] == target:
                    leftPtr -= 1
                leftPtr += 1

                rightPtr = middle
                while rightPtr < len(nums) and nums[rightPtr] == target:
                    rightPtr += 1
                rightPtr -= 1

                return [leftPtr, rightPtr]
            elif nums[middle] < target:
                left += 1
            elif nums[middle] > target:
                right -= 1 
        return [-1,-1]