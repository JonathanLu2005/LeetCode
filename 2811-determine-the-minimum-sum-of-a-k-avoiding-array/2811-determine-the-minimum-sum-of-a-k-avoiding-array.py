class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # array of pos int is k avoiding if no pair that sum to k
        # min possible sum of k avoiding n array

        # be greedy af
        # cant i just go from 1 to whatever
        # until the set is of length n
        # and for each value do k - value and see if in set
        # if not we're chilling
        # should be min
        # prioritise smallest values

        result = set()
        num = 1
        while len(result) < n:
            if k - num not in result:
                result.add(num)
            num += 1

        return sum(result)