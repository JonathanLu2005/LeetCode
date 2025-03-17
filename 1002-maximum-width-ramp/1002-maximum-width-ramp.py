class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxRight = [0] * len(nums)
        i = len(nums) - 1
        prevMax = 0
        for number in reversed(nums):
            maxRight[i] = max(number, prevMax) 
            prevMax = maxRight[i]
            i -= 1

        result = 0

        l = 0
        for r in range(len(nums)):
            while nums[l] > maxRight[r]:
                l += 1
            result = max(r-l, result)

        return result

        """
        # have l and r
        # l is start, r is next
        # if r isnt doing well, keep moving it up
        # if theres a smaller l, take that instead
        # as it enables more possible ramps

        # idea is bad bc it swaps l when we dont ned it to
        # so we wanna store the max avlue to right of each number
        # to avoid moving l that break it 
        l = 0
        r = 1
        result = 0

        while r < len(nums):
            if nums[l] <= nums[r]:
                result = max(result, r-l)
            elif nums[l] > nums[r]:
                l = r
            r += 1

        return result
        """