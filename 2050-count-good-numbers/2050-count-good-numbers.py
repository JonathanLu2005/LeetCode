class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # permutations
        mod = 10 ** 9 + 7
        
        even = (n+1) // 2
        odd = n // 2

        v1 = pow(4, odd, mod)
        v2 = pow(5, even, mod)
        return (v1 * v2) % mod