class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # we can choose 2 adjacents elements in matrix and multiply each by -1
        # goal is to max sum of matrix elements
        # so if there's an even amount of negatives, we can make them all positive
        # otherwise we gotta make the biggest one positives
        neg = 0
        smallest = float("inf")
        result = 0

        n = len(matrix)

        for i in range(0,n):
            for j in range(0,n):
                x = matrix[i][j]

                if x < 0:
                    neg += 1
                    x *= -1
                
                result += x
                smallest = min(smallest,x)

        if neg % 2 == 0:
            return result
        return result - (smallest * 2)