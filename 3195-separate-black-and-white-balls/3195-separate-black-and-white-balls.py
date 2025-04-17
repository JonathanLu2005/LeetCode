class Solution:
    def minimumSteps(self, s: str) -> int:
        # swap adjacent
        # want 1 side to be either colour
        # return min steps
        
        # righ tto left, count number of 0
        # encounter 1, add count to result
        # 100100
        # 2, 1 will need make 2 swaps
        # 4, 1 need make 4 swaps
        result = 0

        ptr = len(s) - 1
        counter = 0
        while ptr >= 0:
            if s[ptr] == "0":
                counter += 1
            else:
                result += counter
            ptr -= 1
        return result