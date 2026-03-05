class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        # apply merge op until no more
        # if 2 adjacenet element equal, chooes leftmost pair, and replace with their sum
        # repeat until no more can be done
        # do index based, if we realise the guy on right is the same, then we merge
        # and once we merge, check guy on left if we just created a new left most pair and merge
        # and keep going until we reach the last element
        n = len(nums)
        i = 0

        while i < (n-1):
            if nums[i] == nums[i+1]:
                value = nums[i] * 2
                nums[i] = value
                nums.pop(i+1)
                i = max(0,i-1)
                n -= 1
            else:
                i += 1
        return nums
        