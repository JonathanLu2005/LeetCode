class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # queries l to r
        # select queries between l to r
        # decrement values by 1
        # zero array is when all elements are 0
        # return true if possible to transofrm
        # if at 0 dont decrement anymore
        # prefix sum question
        n = len(nums)
        subtract = [0] * (n+1)

        for [x,y] in queries:
            subtract[x] += 1
            subtract[y+1] -= 1

        current = 0
        result = 0
        for i in range(0,n):
            current += subtract[i]
            nums[i] = max(nums[i] - current, 0)
            result += nums[i]

        return (result == 0)
