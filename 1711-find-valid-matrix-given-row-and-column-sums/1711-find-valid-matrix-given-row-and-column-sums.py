class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # 3 0
        # 8 0

        # now to get 4 7
        # everything in first col is 11 so remove smth
        # 3 0
        # 1 7

        # 5 0 0
        # 7 0 0
        # 10 0 0
        # need 8, keep 5 3, move 4 and 10
        # need 6, keep 4 and 2, move 8

        # go through colsum and figure out what it needs
        columns = [[0 for x in range(0, len(rowSum))] for x in range(0, len(colSum))]
        for i in range(0, len(colSum)):
            number = colSum[i]
            for j in range(0, len(rowSum)):
                if rowSum[j] > 0:
                    if number >= rowSum[j]:
                        columns[i][j] = rowSum[j]
                        number -= rowSum[j]
                        rowSum[j] = 0
                    else:
                        columns[i][j] = number
                        rowSum[j] -= number
                        break
        
        rotated = [list(row) for row in zip(*columns)]
        return rotated