class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        amount = len(nums) / 3

        hashmap = {}

        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1
        
        result = [key for key, value in hashmap.items() if value > amount]
        return result