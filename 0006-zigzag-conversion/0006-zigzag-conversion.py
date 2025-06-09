class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # generate each row and store values there
        # if we're in a column/line, then we add first x
        # afterwards for the diagonal, we add between 1 - n, so like 2 3
        # then back to column
        # while loop, add first numrows, then add the columns
        # stop till run out of letters
        grid = [[] for _ in range(numRows)]
        n = len(s)
        i = 0

        while i < n:
            # first num rows
            for x in range(numRows):
                if i == n:
                    break

                grid[x].append(s[i])
                i += 1

            # then for diagonal
            for x in range(numRows - 2, 0, -1):
                if i == n:
                    break

                grid[x].append(s[i])
                i += 1

        result = ""

        for row in grid:
            result += "".join(row)
        return result

