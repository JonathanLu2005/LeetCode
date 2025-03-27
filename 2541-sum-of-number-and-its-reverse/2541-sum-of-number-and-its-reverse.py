class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:

        for number in range(0, num + 1):
            
            if number + int(str(number)[::-1]) == num:
                return True
        return False