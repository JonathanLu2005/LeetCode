class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # just go reverse, if its 9 and we add 1, we add 0 and go onwards to keep adding 1
        # else we add 1 and return
        n = len(digits)

        for i in range(n-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0,1)
        return digits