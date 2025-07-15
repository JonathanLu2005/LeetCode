class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # go through all contiguous subarrays 
        # then get max and small
        # could hold max and min and update as we go along
        # do 1, then 1 2 - 2, then 1 2 3 - 2 3 - 3
        hashmap = {}
        n = len(nums)
        res = 0

        for i in range(0,n):
            v = nums[i]

            hashmap[i] = [v,v]

            for j in range(0,i):
                hashmap[j][0] = min(hashmap[j][0],v)
                hashmap[j][1] = max(hashmap[j][1],v)

                res += hashmap[j][1] - hashmap[j][0]

        return res