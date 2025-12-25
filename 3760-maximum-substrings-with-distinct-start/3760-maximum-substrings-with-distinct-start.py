class Solution:
    def maxDistinct(self, s: str) -> int:
        # find number substrings
        # then find number with distinct
        # so basically its number of distinct characters
        myset = set()

        for x in s:
            myset.add(x)

        return len(myset)