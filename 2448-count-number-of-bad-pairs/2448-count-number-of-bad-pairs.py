class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # i j where i < j and condition
        # j - i != nums[j] - nums[i]
        # nums[i] - i != nums[j] - j
        # count times this appears
        # kinda ass, so we just do opposite, then take away from num of possible pairs
        # so try find those that r same then take away from res
        n = len(nums)
        res = (n * (n-1)) / 2
        hashmap = {}


        for i in range(0, n):
            v = nums[i] - i
            hashmap[v] = hashmap.get(v,0) + 1

        for key, value in hashmap.items():
            res -= (value * (value-1)) / 2

        return int(res)