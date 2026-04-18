class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # ok so conseuctive is incremental by 1
        # so we sort it, and we can skip elements too
        # sort it, we traverse, if its incrementing by 1, we include it
        # if its the same, we just ignore
        # and moment we hit a number that isnt incrementing by 1,we store this result and reset coutner and continue
        if not nums:
            return 0

        nums = sorted(nums)
        total = 0

        result = 1
        previousX = nums[0]

        for i in range(1,len(nums)):
            x = nums[i]

            if x - previousX == 1:
                result += 1
            elif x - previousX == 0:
                continue
            else:
                total = max(result,total)
                result = 1

            previousX = x
        
        total = max(result,total)
        return total