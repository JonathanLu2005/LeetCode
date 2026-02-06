class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        # just get all of the maximum and minimum
        # to be cheeky and succeed, we want to get all of the maximum > minimum
        # whilst not scricing the crazy maximums
        # eg if we had 5 4 3 2
        # 1 3 3 4
        # 1 -> 3
        # 3 -> 4
        # 4 -> 3
        # 3 -> 1
        # return 2
        # 4 -> 1
        # return 1
        nums = sorted(nums)
        result = 0

        n = len(nums)

        i = 0
        j = 1
        while i < n and j < n:
            value = nums[i]
            compare = nums[j]

            if compare > value:
                result += 1
                i += 1
                j += 1
            else:
                j += 1
        return result
            
