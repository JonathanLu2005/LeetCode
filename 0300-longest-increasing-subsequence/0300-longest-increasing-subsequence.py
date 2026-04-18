class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        result = [1] * n

        for i in range(1,n):
            v = nums[i]
            current = 1
            for j in range(i):
                x = nums[j]

                if v > x:
                    current = max(current,1 + result[j])

            result[i] = current

        return max(result)