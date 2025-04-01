class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # bottom up
        # idea is figure out if the indices we're on is a 1
        # if so can check to its top left, left, and above and get min
        # e.g if left is 0 means 0 + 1 aka cant have a 2 by 2 square
        # if min is 1 means we can, if mins 2 meanswe're about to form a 3 by 3 square
        # for these things need to think about it in a weird different way to visualise whats going on
        # tehn use the work we've done to avoid repeating work
        rows, cols = len(matrix), len(matrix[0])
        dp = defaultdict(int)

        res = 0
        for r in range(rows):
            cur_dp = defaultdict(int)
            for c in range(cols):
                if matrix[r][c]:
                    cur_dp[c] = 1 + min(
                        dp[c],
                        cur_dp[c-1],
                        dp[c-1]
                    )
                    res += cur_dp[c]
            dp = cur_dp
        return res



        # top down
        """ 
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r,c):
            if r == rows or c == cols or not matrix[r][c]:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]

            cache[(r,c)] = 1 + min(
                dfs(r+1,c),
                dfs(r, c+1),
                dfs(r+1, c+1)
            )
            return cache[(r,c)]

        res = 0
        for r in range(rows):
            for c in range(cols):
                res += dfs(r,c)
        return res
        """