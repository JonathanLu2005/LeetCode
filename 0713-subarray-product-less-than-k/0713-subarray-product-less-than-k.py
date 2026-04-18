class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # key thing is that instead of doing the weird equation
        #we j ust simpyladd as 5 2 6 work
        # so its just 5 2 6, 3 options
        # then 2 6, 2, then 6 1
        # yeah because if we had 5 2 6 10, 5 2 6 work, 2 6 10 imagine work, we repeat 2 6
        if k <= 1:
            return 0

        current = 1
        length = 0
        l = 0
        result = 0

        for x in nums:
            current *= x
            length += 1

            while current >= k:
                result += length - 1
                length -= 1
                current = current / nums[l]
                l += 1

        result += ((length + 1) * length) / 2
        return int(result)