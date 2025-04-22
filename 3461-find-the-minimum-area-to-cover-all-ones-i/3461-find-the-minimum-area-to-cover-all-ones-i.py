class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # find smallest area that covers all of the 1s
        # check each row, find the farthest 1 (column)
        # and try to find the lowest row (row)
        # get the min first, and the max, that'll determine the bounaries
        # because if there's first few rows bunch of 0s then ignore

        minRow = float("inf")
        minCol = float("inf")
        farthestRow = 0
        farthestColumn = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                value = grid[row][column]

                if value == 1:
                    minRow = min(minRow, row+1)
                    minCol = min(minCol, column+1)
                    farthestRow = max(farthestRow, row+1)
                    farthestColumn = max(farthestColumn, column+1)

        return (farthestRow - minRow + 1) * (farthestColumn - minCol + 1)