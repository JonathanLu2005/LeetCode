class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # magic square
        # distinct numbers
        # 3 by 3
        # row, column, diagonals, have same sum

        # could brute force, can also pre compute
        # dunno if that makes life easier

        # for n rows, we traverse n-2 rows
        # then look at rows at n+1, n+2
        # for columns, we do n - 2 columns and same above?
        res = 0


        if len(grid) < 3 or len(grid[0]) < 3:
            return res

        legalNumbers = set([1,2,3,4,5,6,7,8,9])

        for row in range(0, len(grid) - 2):
            for col in range(0, len(grid[0]) - 2):
                rowMap = {}
                colMap = {}
                diagonalMap = {}

                rowMap[1] = grid[row][col] + grid[row][col+1] + grid[row][col+2]
                rowMap[2] = grid[row+1][col] + grid[row+1][col+1] + grid[row+1][col+2]
                rowMap[3] = grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2]

                colMap[1] = grid[row][col] + grid[row+1][col] + grid[row+2][col]
                colMap[2] = grid[row][col+1] + grid[row+1][col+1] + grid[row+2][col+1]
                colMap[3] = grid[row][col+2] + grid[row+1][col+2] + grid[row+2][col+2]

                diagonalMap[1] = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]
                diagonalMap[2] = grid[row+2][col] + grid[row+1][col+1] + grid[row][col+2]

                numbers = set([grid[row][col], grid[row][col+1], grid[row][col+2],
                            grid[row+1][col], grid[row+1][col+1], grid[row+1][col+2],
                            grid[row+2][col], grid[row+2][col+1], grid[row+2][col+2]
                ])

                lengths = set([rowMap[1], rowMap[2], rowMap[3], colMap[1], colMap[2], colMap[3], diagonalMap[1], diagonalMap[2]])

                if len(numbers) == 9 and len(lengths) == 1 and numbers == legalNumbers:
                    res += 1

        return res

                

