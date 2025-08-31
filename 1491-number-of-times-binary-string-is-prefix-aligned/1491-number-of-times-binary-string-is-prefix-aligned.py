class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        # given array where to flip
        # prefix aligned iff prefix is 1s and rest are 0s
        # store the largest thats flipped
        # s.t. everything before it must be flipped too
        # can testify by summing everything and seeing if its all
        # equal to n + n-1 + n-2 ... aka n(n+1) / 2
        mx = -1
        result = 0
        flipped = set()
        total = 0

        for x in flips:
            if x in flipped:
                flipped.remove(x)
                mx = max(flipped)
                total -= x
            else:
                mx = max(mx,x)
                flipped.add(x)
                total += x

            if total == ((mx * (mx+1)) / 2):
                result += 1

        return result