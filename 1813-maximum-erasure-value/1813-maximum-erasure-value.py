class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # have pos int
        # erase subarray with unqiue lemes
        # score erasing subarray = sum of elements
        # return max score by erasing 1 subarray
        # can keep going, moment we hit same value (no longer unique)
        # we store score, pop everything out, and continue on?
        result = 0
        current = 0
        visited = set()
        l = 0

        for x in nums:
            # no longer unique
            if x in visited:
                result = max(result,current)

                while x in visited:
                    val = nums[l]
                    current -= val
                    visited.remove(val)
                    l += 1
            current += x
            visited.add(x)
        return max(result,current)
                

