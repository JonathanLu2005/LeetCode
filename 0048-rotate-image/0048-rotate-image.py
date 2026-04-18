class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        newMatrix = [list(reversed(row)) for row in zip(*matrix)]

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                matrix[row][col] = newMatrix[row][col]