class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # isnt this legit finding a subarray with the max and min value
        maxValue = max(nums)
        minValue = min(nums)

        return k * (maxValue - minValue)