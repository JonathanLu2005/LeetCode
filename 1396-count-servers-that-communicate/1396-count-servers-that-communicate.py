class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # store number of computers on each row and column
        # then for aech node check if theres another
        # if so thats cool result += 1, else nah
        rowmap = {}
        columnmap = {}

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    rowmap[row] = rowmap.get(row,0) + 1
                    columnmap[column] = columnmap.get(column,0) + 1

        result = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1 and (rowmap.get(row,0) > 1 or columnmap.get(column,0) > 1):
                    result += 1
        return result
                    

