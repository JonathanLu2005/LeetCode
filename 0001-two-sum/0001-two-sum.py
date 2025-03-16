class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # what he does differently is instead of filling the entire hashmap
        # he goes through them, see if the other exist, if not, then add to hashmap
        # solves the need for checking if its same
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        """


        hashmap = {}

        for i in range(0, len(nums)):
            hashmap[nums[i]] = i 

        for x in nums:
            if target - x in hashmap and nums.index(x) != hashmap[target-x]:
                return [nums.index(x), hashmap[target-x]]
        """