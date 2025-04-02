class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # brute force is legit finding all subsets and finding the biggest one
        # thats divisible by 3

        # dp store 3, 1 for remainder 0, remainder 1, then 2, and store largest
        # such that when we make our thing and need to add x with remainder y to get to div by 3
        # can access it

        dp = [0,0,0]
        for num in nums:
            # need copy so we can get all numbers
            for i in dp[:]:
                dp[(i+num)%3] = max(dp[(i+num)%3], i + num)
        return dp[0]

        # idea is that for each number we apply to each
        # in index 0 1 2
        # see if its better and we store
        # in case we wanna use later
        # i think dp like these need u to find a human way
        # to solve it efficiently
        # then write it in code