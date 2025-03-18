class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]

        array = [1,1]
        rowIndex -= 1

        def recursion(index):
            nonlocal array
            if index == 0:
                return array

            new = []
            for x,y in zip(array[0:], array[1:]):
                new.append(x+y)
            new.insert(0,1)
            new.append(1)

            array = new
            recursion(index-1)

        recursion(rowIndex)
        return array
        #return array[-1]