class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if samewe can skip as we dont care
        if not nums:
            return 0
        nums = sorted(nums)
        result = 1
        current = 1
        prev = nums[0]

        for i in range(1,len(nums)):
            cur = nums[i]

            if cur - prev == 1:
                current += 1
                prev = cur
            elif cur - prev == 0:
                continue
            else:
                result = max(result,current)
                current = 1
                prev = cur
        result = max(result,current)
        return result
                