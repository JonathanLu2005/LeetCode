class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # each count is 1
        # and with te next vale look back and take the largest count iff they're larger then them
        # as that'sthe best choice so far
        n = len(nums)
        result = [1] * n
        #print(result)

        for i in range(0,n):
            value = nums[i]
            res = 0

            for j in range(0,i):
                if nums[j] < value:
                    res = max(res,result[j])

            result[i] += res
        #print(result)
        return max(result)
