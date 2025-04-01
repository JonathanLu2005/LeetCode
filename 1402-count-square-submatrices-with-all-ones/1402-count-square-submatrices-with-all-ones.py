class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # bottom up
        rows, cols = len(matrix), len(matrix[0])
        dp = defaultdict(int)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]:
                    dp[(r,c)] = 1 + min(
                        dp[(r-1,c)],
                        dp[(r,c-1)],
                        dp[(r-1,c-1)]
                    )
                    res += dp[(r,c)]
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