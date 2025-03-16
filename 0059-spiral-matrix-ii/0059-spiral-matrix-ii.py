class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]

        # right, down, left, up
        row = 0
        column = 0

        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        direction = 0

        for number in range(1, (n**2) + 1):
            if direction == 0 and (column + 1 == n or grid[row][column+1] != 0):
                direction = 1
            elif direction == 1 and (row + 1 == n or grid[row+1][column] != 0):
                direction = 2
            elif direction == 2 and (column - 1 == -1 or grid[row][column-1] != 0):
                direction = 3
            elif direction == 3 and (row - 1 == -1 or grid[row-1][column] != 0):
                direction = 0

            grid[row][column] = number
            row += directions[direction][0]
            column += directions[direction][1]

        return grid