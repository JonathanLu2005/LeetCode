class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # have set of all possible column and row
        # traverse matrix, moment its 0, we turn th whole row and column 0
        # HOWEVER, we store the column and row thats been set to 0
        # so if its another column then its like yh we ignore
        # actually, as we go along, when we find 0, we store the row and column
        # so the moment we get to next coordinate, if its part of row and column we set 0
        # mmm but idk we might miss some
        # find where all row and column 0 are, then set it all 0?
        row = set()
        column = set()

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    row.add(x)
                    column.add(y)

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if x in row or y in column:
                    matrix[x][y] = 0