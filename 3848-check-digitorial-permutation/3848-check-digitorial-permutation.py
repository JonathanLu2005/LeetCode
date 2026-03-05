class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        # sum of factorial == number
        # any permutation of n form digitorial number
        # true else false
        # i mean, we can do this
        # traverse number, calculate the factorial, and keep count of every guy
        # then when we have the final factorial sum, we check the count and if it matches the othe rcount we're good
        n = str(n)
        result = 0
        original = {}
        store = {}

        def calculate(n):
            number = 1

            for x in range(1,n+1):
                number *= x
            
            store[n] = number
            return number

        for x in n:
            original[x] = original.get(x,0) + 1
            
            x = int(x)

            if x in store:
                result += store[x]
            else:
                result += calculate(x)

        result = str(result)
        factorial = {}

        for x in result:
            factorial[x] = factorial.get(x,0) + 1

        return (factorial == original)