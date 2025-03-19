class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap = {}
        keys = set(nums)

        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1

        res = []

        for x in keys:
            if hashmap[x] == 1:
                res.append(x)

        return res
