class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # if we know 5 2 6 are all < 100, so 60
        # that means 5 2 6, 5 2, 2 6, and 5 2 6 are valid
        # which is the equivalent of 3 (3 + 1) / 2
        # 10 5, 2 (2 + 1) / 2 = 3
        # issue is that we're counting 5 again, so we do the above calculation but minus length
        # to only considefr pair
        # then as we go for each x we can increment result if they're < k
        # and if it above, we keep dividing 
        # instead can have variable to hold length and what to remove and current to remove the extra array
        # 
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