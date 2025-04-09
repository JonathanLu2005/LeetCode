class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
       # have a grid
       # follow the steps in arr
       # and return smallest index in arr when we have completey painted a row or column
       # need track each row and column
       
       # very brute force, make a row and column grid like mat
       # then for x in arr, we keep removing
       # and moment we get [] we're cool
       
       # faster is having frequency and keep subtracting till we get 0
       # could do
       # row1 = x, row2 = y, row3 = z
       # col1 = x, col2 = y, col3 = z
       # and each number find what row and col they're in
       # such that for aech number, we get their row and col, and do minus
       # brute force = O(n^3), this O(n^2)

        rowHashmap = {}
        colHashmap = {}
        indexHashmap = {}

        for row in range(len(mat)):
            rowHashmap[row] = 0

            for col in range(len(mat[0])):
                rowHashmap[row] += mat[row][col]
                colHashmap[col] = colHashmap.get(col,0) + mat[row][col]
                indexHashmap[mat[row][col]] = [row, col]

        for i in range(0, len(arr)):
            value = arr[i]

            row, col = indexHashmap[value]

            rowHashmap[row] -= value
            colHashmap[col] -= value

            if rowHashmap[row] == 0 or colHashmap[col] == 0:
                return i
        


