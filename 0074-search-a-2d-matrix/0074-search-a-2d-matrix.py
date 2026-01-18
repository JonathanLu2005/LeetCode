class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row which target is between and move on fromthat

        for array in matrix:
            if target in range(array[0],array[-1]+1):
                p1 = 0
                p2 = len(array)-1

                while p1 <= p2:
                    mid = int((p1 + p2) / 2)
                    value = array[mid]

                    if value == target:
                        return True
                    elif value < target:
                        p1 = mid + 1
                    else:
                        p2 = mid - 1
        return False