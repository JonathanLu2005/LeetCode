class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # live = 1, dead = 0
        # cell has 8 neighobur
        # live cell with < 2 live neighbour = die
        # live cell with 2 or 3 live neighbour live on
        # live cell with more than 3 live neighbour die
        # dead cel with 3 live enighbor live
        boardCopy = [row[:] for row in board]

        rows = len(boardCopy)
        columns = len(boardCopy[0])

        def solve(row, column):
            directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,-1], [-1,1]]

            alive = 0

            for x, y in directions:
                r = row + x
                c = column + y

                if (r in range(rows)) and (c in range(columns)) and boardCopy[r][c] == 1:
                    alive += 1

            if boardCopy[row][column] == 1:
                if alive < 2:
                    return 0
                elif alive > 3:
                    return 0
                else:
                    return 1
            else:
                if alive == 3:
                    return 1
                return 0

        for x in range(rows):
            for y in range(columns):
                board[x][y] = solve(x,y)