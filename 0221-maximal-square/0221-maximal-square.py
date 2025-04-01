class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # do bottom up and work through the bottom edge of the square
        # get the min of its left, top left, and above
        # if its 1 meaning all are 1 or more, means we can make a 2 by 2 square
        # vice versa if its 2 or 0
        # we're able to do the work as we go through the grid and avoid repeating it
        # as we're going bottom up
        # then return whatevers the max whilst we do work
        rows, cols = len(matrix), len(matrix[0])

        dp = defaultdict(int)

        res = 0
        # cehck each square
        for r in range(rows):
            for c in range(cols):
                # if we're on a 1 we can bother, else its set to 0
                if int(matrix[r][c]) == 1:
                    # with logic discussed above, able detect if we can make a 1 by 1 square or 2 by 2 etc
                    dp[(r,c)] = 1 + min(
                        dp[(r,c-1)],
                        dp[(r-1,c)],
                        dp[(r-1,c-1)]
                    )

                    res = max(res, dp[(r,c)])
        return res * res