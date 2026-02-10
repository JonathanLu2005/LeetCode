class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        # largest element after merg ops
        # nums = pos ints
        # choose i s.t. i <= i + 1
        # replace i + 1 with i + (i+1) and delete i
        # return largest value possible
        # so... with i and i + 1
        # we can only make i + 1 as i + i + 1, iff i <= i + 1
        # so to get more of the values from the LHS, to get added up to a value from RHS
        # we want to try our best to exploit the fact we can add a smaller element to left to a larger element to right
        # we do that so our right is so big that whatever is on left has no choice but to get added to right
        # largerelement
        # and if we cant do it s.t. theres a bigger number, we use that number and continue instead
        # keep doing that until ther's no left
        # and if its just decreasing like 4 3 2 1, bc we iterate through, it checks all
        if not nums:
            return 0

        result = nums[-1]
        n = len(nums)
        j = n-2

        current = nums[-1]

        while j >= 0:
            nextValue = nums[j]

            if current >= nextValue:
                current += nextValue
            else:
                result = max(result,current)
                current = nums[j]
            j -= 1
        result = max(result,current)
        return result

