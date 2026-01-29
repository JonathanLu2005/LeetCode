class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        result = [-1] * n
        divider = (k*2) + 1

        if divider > n:
            return result

        value = 0
        i = 0

        while i < divider:
            value += nums[i]
            i += 1
        
        result[k] = int(math.floor(value / divider))
        for i in range(k+1,n-k):
            value += nums[i+k]
            value -= nums[i-k-1]
            result[i] = int(math.floor(value / divider))
        return result



        