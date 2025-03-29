class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True] * (n+1)
        prime[0] = False
        prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for multiple in range(i*i, n+1, i):
                    prime[multiple] = False

        result = []

        for x in range(2, n // 2 + 1):
            if prime[n-x] and prime[x]:
                result.append([x, n-x])
        return result
