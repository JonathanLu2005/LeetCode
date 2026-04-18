class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        # i mean just lienar innit
        result = 0
        digit = str(digit)

        for x in nums:
            for y in str(x):
                if y == digit:
                    result += 1

        return result