class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}

        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1

            if hashmap[x] == 2:
                return x