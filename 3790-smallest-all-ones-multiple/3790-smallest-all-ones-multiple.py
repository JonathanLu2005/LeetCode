class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        # given k
        # smallest int n divisible by k
        # only 1
        # return number of digits needed
        # else -1
        # n % k == 0
        
        # do rem = 1 % k
        # then rem = (rem * 10 + 1) % k
        # counting number 1 been added
        # continue until rem == 0 or rem repeats
        repeats = set()
        result = 1

        rem = 1 % k
        repeats.add(rem)

        while True:
            if rem == 0:
                return result
            rem = (rem * 10 + 1) % k
            result += 1

            if rem in repeats:
                return -1
            repeats.add(rem)
