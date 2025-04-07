class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # given n, we immediately know the largest we could get is n - 2 from middle
        # perhaps we could check that and realise n-2 is not possible
        # so we try n-2 -1 and so on until its not possible

        # thing is that the brute force is we go through the grid
        # and we just see if left, below, above, right, are 1 aka a plus is possible
        # im just wondering how i can store it in a way with the grid
        # so we can dp it
        # bc thats the brute force way, must be a way to cache with the grid too

        # hint is that we've 4 of these grids, and we calculate the number of 1s to the left
        # number of 1s to the right
        # then when we go through our grid, we just take min of left, right, up, above
        # so we know to figure out the power of a plus, we look at left right below above
        # store that somewhere so we can access again ourselves

        # figre out how to brute force it, then optimise is by figuring out how can we store
        # any computations to easily use later

        # important using for _ in range to avoid shallow copies
        if n <= 2:
            if len(mines) != (n * n):
                return 1
            return 0
        
        grid = [[1] *n for _ in range(n)] 
        for r, c in mines:
            grid[r][c] = 0

        leftGrid = [row[:] for row in grid]
        rightGrid = [row[:] for row in grid]
        aboveGrid = [row[:] for row in grid]
        belowGrid = [row[:] for row in grid]

        # top left to bottom right
        for row in range(n):
            for column in range(n):
                if grid[row][column] == 1:
                    if column > 0:
                        leftGrid[row][column] += leftGrid[row][column - 1]

                    if row > 0:
                        aboveGrid[row][column] += aboveGrid[row - 1][column]

        # bottom left to top right
        for row in range(n - 1, -1, -1):
            for column in range(n - 1, -1, -1):
                if grid[row][column] == 1:
                    if column + 1 < n:
                        rightGrid[row][column] += rightGrid[row][column + 1]
                    
                    if row + 1 < n:
                        belowGrid[row][column] += belowGrid[row + 1][column]

        result = 0

        for row in range(0, n):
            for column in range(0, n):
                # possible square
                # find square how much it has from each direction
                if grid[row][column] == 1:
                    squarePower = min(
                        leftGrid[row][column],
                        rightGrid[row][column],
                        aboveGrid[row][column],
                        belowGrid[row][column]
                    )

                    result = max(result, squarePower)


        return result