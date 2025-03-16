class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)

        minus = 1
        if x[0] == "-":
            minus = -1
            x = x[1:]


        x = x[::-1]
        x = int(x)

        if x < -(2)**31 or x > ((2)**31) -1:
            return 0
        return x * minus