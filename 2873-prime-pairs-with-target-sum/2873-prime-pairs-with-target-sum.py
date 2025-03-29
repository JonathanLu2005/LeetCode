class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True] * (n+1)
        prime[0] = False
        prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for multiple in range(i*i, n+1, i):
                    prime[multiple] = False
        hashmap = {num: num for num in range(n+1) if prime[num]}


        result = []

        for x in range(2, int(n/2) + 1):
            if n-x in hashmap and x in hashmap:
                result.append([x, n-x])
        return result