class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # ok have to choose 3 elements to multiply
        # and replace 1 guy as well
        # tactic is
        # get the 2 biggest pos numbers times 10^5
        # get the 2 biggest neg number times 10^5
        # get the biggest pos and biggest neg number times -10^5
        # or its 0 if there's only 2 non 0 numbers we can have
        nums = sorted(nums)
        biggestneg = nums[0] * nums[1]
        biggestpos = nums[-1] * nums[-2]
        biggestmix = nums[0] * nums[-1]

        multiplier = 10**5

        if abs(biggestneg) > abs(biggestpos):
            if abs(biggestneg) > abs(biggestmix):
                # biggest neg best
                return biggestneg * multiplier
            else:
                # biggest mix
                return biggestmix * -1 * multiplier
        elif abs(biggestmix) > abs(biggestpos):
            # biggestmix best
            return biggestmix * -1 * multiplier
        else:
            # biggest pos best
            return biggestpos * multiplier