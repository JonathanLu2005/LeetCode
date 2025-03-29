class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        prime = [True] * (n)
        prime[0] = prime[1] = False

        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                for multiple in range(i*i, n, i):
                    prime[multiple]=False
        
        return prime.count(True)