class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        target = len(nums) / 2
        hashmap = {}

        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1
            if hashmap[x] == target:
                return x