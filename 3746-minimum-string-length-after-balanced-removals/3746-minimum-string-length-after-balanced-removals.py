class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        # remove any substring s.t. num a = num b char
        # remaining part concatenated
        # just get length, count number of a and b, get minimum of that, and take it away from the length times 2?
        a = 0
        b = 0
        n = 0

        for x in s:
            if x == "a":
                a += 1
            else:
                b += 1
            n += 1
        res = min(a,b)
        return n - (2 * res)