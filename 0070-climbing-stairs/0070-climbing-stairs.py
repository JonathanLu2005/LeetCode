class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1

        for i in range(n-1):
            # adding in previous 2 values
            temp = one
            # store temp for one
            one = one + two
            two = temp
            # pdate one then two is one but before

        return one


        """
        res = 0
        

        def backtrack(path):
            if path == n:
                nonlocal res
                res += 1
                return
            if path > n:
                return

            path += 1
            backtrack(path)
            path += 1
            backtrack(path)

        backtrack(0)
        return res
"""
            