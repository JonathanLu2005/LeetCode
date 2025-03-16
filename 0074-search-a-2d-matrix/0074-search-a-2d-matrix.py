class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first check if the target is within the range of the array
        # if its smaller, go down an array, if its bigger, go up an array
        # then do regular thingy in the array

        arrLeft = 0
        arrRight = len(matrix) - 1

        while arrLeft <= arrRight:
            arrMid = (arrLeft + arrRight) // 2
            arr = matrix[arrMid]
            left = 0
            right = len(arr) - 1

            if target < arr[left]:
                arrRight = arrMid - 1
            elif target > arr[right]:
                arrLeft = arrMid + 1
            else:

                while left <= right:
                    mid = (left + right) // 2
                    val = arr[mid]

                    if target < val:
                        right = mid - 1
                    elif target > val:
                        left = mid + 1
                    elif target == val:
                        return True
                return False
        return False




























        """
        # so we have x many arrays
        # l = 0, r = far right
        # mp = middle
        # access that array
        # if our target is less than the far left
        # that means l = 0, r = mp - 1 (not in far right of matrix)
        # if array right is > target, not in this array, l = mp + 1
        # do this until we get the right array
        # then just binary search through

        # overall idea is find the array that the number shoudl be in
        # if its in there, then search for it
        # if in true, else false
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        # trying find row (top is our left, bot is our right)
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                # target may be in array
                break

        # none of rows contains
        if not (top <= bot):
            return False
        # this is how make it faster, instead of nested whiles
        # just braek if we found it
        # check if exist, else go wth row

        if not (top <= bot):
            return False 
        row = (top + bot) // 2
        l, r = 0, COLS -1
        # then regular binary search in array
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        """

        """


        left = 0
        right = len(matrix) - 1

        while left <= right:
            middle = (left + right) // 2
            arr = matrix[middle]

            arrLeft = 0
            arrRight = len(arr) - 1

            if target < arr[arrLeft]:
                right = middle - 1
            elif target > arr[arrRight]:
                left = middle + 1
            else:
                # we're in the correct array now
                while arrLeft <= arrRight:
                    arrMiddle = (arrLeft + arrRight) // 2

                    if arr[arrMiddle] > target:
                        arrRight = arrMiddle - 1
                    elif arr[arrMiddle] < target:
                        arrLeft = arrMiddle + 1
                    else:
                        return True
                return False
        return False"""