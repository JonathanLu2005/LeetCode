class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # 3 stones at a b c
        # move a stone from end point
        # x y z s.t. x < y < z
        # move either x or z between x and z which isnt y
        # end when u cant make any more moves so 3 consecutive positions
        # we have min and max moves we can play
        # return that
        # 1        5         10
        # minimum => number of moves to get to y right, so could be 0-2
        # maximum move is number times we can keep moving it, so 5-1-1 + 10-5-1
        # mmm
        # minimum moves is 0 if they're next, 1 if 1 of endpoint is 1 away from the middle, 2 if neither of situation
        left = min(a,min(b,c))
        right = max(a,max(b,c))

        if left == a and right == c or left == c and right == a:
            middle = b
        elif left == b and right == c or left == c and right == b:
            middle = a
        else:
            middle = c

        result = []

        if middle - left == 1 and right - middle == 1:
            result.append(0)
        elif middle - left <= 2 or right - middle <= 2:
            result.append(1)
        else:
            result.append(2)

        maximum = (middle-left-1) + (right-middle-1)
        result.append(maximum)
        return result