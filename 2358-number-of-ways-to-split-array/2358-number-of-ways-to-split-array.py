class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # valid split at index i if followings true
        # sum of first i + 1 elements >= sum of last n -i - 1 elments
        
        firstHalf = 0
        secondHalf = sum(nums)
        result = 0

        nums.pop(-1)
        for x in nums:
            firstHalf += x
            secondHalf -= x

            if firstHalf >= secondHalf:
                result += 1

        return result