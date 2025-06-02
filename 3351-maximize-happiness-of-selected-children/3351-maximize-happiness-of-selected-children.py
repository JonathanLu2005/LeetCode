class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # select k biggest values
        # then as we go through each value, we take away 1 up to k
        # and add, if 0 then add 0
        result = 0

        happiness = sorted(happiness)[::-1]
        n = len(happiness)
        
        for x in range(0, k):
            result += max(happiness[x] - x, 0)
        return result
        