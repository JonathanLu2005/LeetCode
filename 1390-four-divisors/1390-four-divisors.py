class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # for each value, find 4 divisors
        # must have 4 divisors, no more no less
        # and then get them divisor value and sum them up
        # prob some maths and specific values that only has 4 divisors
        # by default values are going to have 1 x itself
        # so need 2 more
        # loop from 1 to sqrt of number to find divisor
        valid = {}
        values = {}
        result = 0

        for x in nums:
            if x in valid:
                if valid[x]:
                    result += values[x]
            else:
                count = 0
                value = 0
                numbers = set()
                for i in range(1, int(math.sqrt(x)) + 1):
                    if x % i == 0:
                        count += 2
                        numbers.add(i)
                        numbers.add(x/i)
                        value += i + (x / i)
                if count == 4 and len(numbers) == 4:
                    result += value
                    values[x] = value
                    valid[x] = True
                else:
                    valid[x] = False
        return int(result)


