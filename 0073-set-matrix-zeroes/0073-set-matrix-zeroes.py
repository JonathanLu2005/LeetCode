class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # traverse everything
        # hold rows and columns that need to become 0
        rows = set()
        columns = set()

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    rows.add(row)
                    columns.add(column)

        for row in rows:
            for column in range(len(matrix[0])):
                matrix[row][column] = 0

        for row in range(len(matrix)):
            for column in columns:
                matrix[row][column] = 0
