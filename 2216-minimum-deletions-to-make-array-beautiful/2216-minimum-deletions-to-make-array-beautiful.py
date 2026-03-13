class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        # nums is even and
        # for every even index, its not the same as the guy to the right
        # for every pair
        # if they're equal, delete one of them
        # issue is we have 2 situations
        # 2 1 1 1 1 5
        #  if we delete index 2, we resolve it
        # if we dlete index 3, wealso resolve it
        # ok my concern was that if we delete 1 or other, it wont chagne anything
        # 2 if we delete that, then wont solve anything, but we just need to delete again

        # lets clear everything out, then delete last guy if all is worse
        n = len(nums)
        i = 0
        result = 0

        while i < n-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                n -= 1
                result += 1
            else:
                i += 2

        if len(nums) % 2 == 1:
            result += 1
        return result
        