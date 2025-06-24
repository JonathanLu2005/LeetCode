class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        # same strat
        result = 0

        l = 0
        current = 1
        length = 0

        for x in nums:
            length += 1
            current *= x

            while current >= k:
                result += (length-1)
                current = current / nums[l]
                length -= 1
                l += 1

        result += (length * (length+1)) / 2
        return int(result)
