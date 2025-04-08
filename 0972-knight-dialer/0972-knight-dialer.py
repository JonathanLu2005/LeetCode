class Solution:
    def knightDialer(self, n: int) -> int:
        # given number pad, and we can only move like a horse
        # find number of distinct phone numbers we can call

        # thing is that its has to do with maths, 
        # because let say we're 1, we've 2 options
        # 6 and 8, and they've 3 and 2 options
        # so its like 2 * 3
        # if n = 1, 1
        # if n = 2, its just whatever x is
        # if n = 3, do x multiply y
        # so if we were to brute force, we choose 1 number, then backtrack with 2 other options, ten other options
        # and keep multiplying and multiplying

        # let say we did just 1 not all cell
        # then we'd do 1, then 6 8, then 1 7 0 3 are our optios and we go and go
        # then we'd do that for next bunch numbers
        # wondering if theres a pattern that we can precompute
        # like if we did n - x calls with 1 number, store value of that, so if we come across that number again
        # we reuse it
        # hashmap store options for each number
        # and also store number calls

        # think decision tree

        # wait if we do 1 and do n number and we end up let say 3, then the answer is same for 3?
        # more thinking about how many digits we can end with x
        # find how many end with x

        if n == 1:
            return 10


        mod = 10**9 + 7
        # wher each number can go to which
        jumps = [
            [4,6],
            [6,8],
            [7,9],
            [4,8],
            [3,9,0],
            [],
            [1,7,0],
            [2,6],
            [1,3],
            [2,4]
        ]
        
        # store number way to end with 0-9
        dp = [1] * 10

        for _ in range(n-1):
            # dont overwrite dp
            nextDP = [0] * 10

            # n is digit we're on
            for n in range(10):
                # find out what other area we can land on
                for j in jumps[n]:
                    # can compute num way land on digit

                    # dp n is number way to land on nth, plus j jump
                    nextDP[j] = (nextDP[j] + dp[n]) 

            dp = nextDP

        return sum(dp) % mod