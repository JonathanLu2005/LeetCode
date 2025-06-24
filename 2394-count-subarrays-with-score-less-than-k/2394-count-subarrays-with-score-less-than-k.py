class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # sliding window, keep counting product and sum and length
        # if not < k, then add length, and take away the far left value and continue
        # once end do the n * n+1 / 2 one
        # main reason why not do n * n+1 / 2 all time is cuz we mgiht repeat subarrays
        result = 0

        length = 0
        total = 0
        l = 0

        for x in nums:
            length += 1
            total += x

            # if >= k we need get rid of far left
            while length * total >= k:
                result += (length-1)
                total -= nums[l]
                length -= 1
                l += 1

        # at end add any remaining subarray left
        result += (length * (length+1)) / 2
        return int(result)
