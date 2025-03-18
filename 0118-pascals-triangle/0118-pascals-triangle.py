class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]

        numRows -= 2
        result = [[1], [1,1]]

        def recursion(numRows, array):
            if numRows == 0:
                return 

            newArray = []

            for x, y in zip(array[0:], array[1:]):
                newArray.append(x+y)
            newArray.insert(0, 1)
            newArray.append(1)

            result.append(newArray.copy())
            recursion(numRows - 1, newArray)



        recursion(numRows, [1,1])
        return result
        