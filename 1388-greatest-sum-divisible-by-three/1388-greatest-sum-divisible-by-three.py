class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # brute force is legit finding all subsets and finding the biggest one
        # thats divisible by 3

        # dp store 3, 1 for remainder 0, remainder 1, then 2, and store largest
        # such that when we make our thing and need to add x with remainder y to get to div by 3
        # can access it

        dp = [0,0,0]
        for num in nums:
            for i in dp[:]:
                dp[(i+num)%3] = max(dp[(i+num)%3], i + num)
        return dp[0]