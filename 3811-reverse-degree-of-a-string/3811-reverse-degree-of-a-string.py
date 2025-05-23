class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(0,n):
            v = s[i]
            t = 26 - (ord(v) - 97)
            res += (i+1) * (t)
        return res