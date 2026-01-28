class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # find max score after alternating it
        # s.t. its - + - + - +
        # its + - + -...
        # so if its odd, its half half + -
        # if it evens
        # 1 2 3 4, its 2 + 1 negative
        # take length and - 1
        # find  the number of negatives we need...
        # 1 2 3 4 5, 2 +, 2 -
        # if its EVEN, its the LENGTH - 1 / 2 ROUND DOWN
        # if its ODD, its the LENGTH - 1, / 2
        # and then we keep the smallest values as the negative, and rest as positive
        array = sorted([x**2 for x in nums])
        length = len(nums)

        if length % 2 == 1:
            amount = int((length - 1) / 2)
        else:
            amount = int(length / 2)

        i = 0
        n = len(array)
        result = 0

        while i < n:
            if i < amount:
                result -= array[i]
            else:
                result += array[i]
            i += 1
        return result
        