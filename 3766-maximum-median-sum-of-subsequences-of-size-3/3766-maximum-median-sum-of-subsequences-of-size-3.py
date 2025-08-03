class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        # for every subsequence taken out, get highest median and calculate
        # sort it first
        # then we know by defaultt he max wont ever be chosen as too big
        # so can get 2nd max
        # then to preserve next max, take the smallest as better choices
        # maybe faster to get the 2nd last, and continue on
        
        nums = sorted(nums)
        res = 0
        c = 0
        n = len(nums) / 3
        i = -2

        while c < n:
            res += nums[i]
            c += 1
            i -= 2

        return res