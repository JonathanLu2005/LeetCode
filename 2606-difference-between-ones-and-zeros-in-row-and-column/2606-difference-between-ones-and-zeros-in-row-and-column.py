class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # find num of 1 in each row and col
        # find num of 0 in each row and col
        # then add all 1s, subtract all 0s

        # i mean, find num of 0 and 1 in each row and col
        # if we find num of 1 in each row, can do row length  - num

        columnLength = len(grid)
        rowLength = len(grid[0])

        hashmapRow = {}
        hashmapColumn = {}

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    hashmapRow[row] = hashmapRow.get(row,0) + 1
                    hashmapColumn[col] = hashmapColumn.get(col,0) + 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                rowOne = hashmapRow.get(row,0)
                colOne = hashmapColumn.get(col,0)
                rowZero = rowLength - rowOne
                colZero = columnLength - colOne

                grid[row][col] = rowOne + colOne - (rowZero + colZero)

        return grid