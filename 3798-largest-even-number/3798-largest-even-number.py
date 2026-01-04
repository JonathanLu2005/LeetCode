class Solution:
    def largestEven(self, s: str) -> str:
        if s == "":
            return s
        while s and s[-1] != "2":
            s = s[:-1]
        return s