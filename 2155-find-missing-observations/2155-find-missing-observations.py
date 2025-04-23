class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # n + m 6 sided dice rolls
        # have face 1-6
        # n observations are missing
        # only have m observatins
        # have average for n + m
        # given array rolls of m, i = ith observation
        # given mean and n
        # return the missing observations
        # so overage is mean
        # if not possible return []

        # mean = for m + n
        # n left
        # given what m is

        # find m sum = 12
        # find m + n = 6
        # 6 * 4 = 24 - 12
        # 12, see if we can get that into n lots from 1-6
        # if not possible and if overflow it, then not possible

        mSum = sum(rolls)
        total = mean * (len(rolls) + n)
        remain = total - mSum

        result = []
        # cases, if our array filled with 6s, is more than n, not possible
        # otherwise we've the answer however
        # if the sum of the result array is < n, not possible, as dont have n 1s
        if remain < n:
            return []

        while remain > 0:
            if remain >= 6:
                result.append(6)
                remain -= 6
            else:
                result.append(remain)
                remain -= remain
            
            if len(result) > n:
                return []

        # else if smaller, we need to space it out
        index = 0
        while len(result) < n:
            if result[index] > 1:
                result.append(1)
                result[index] -= 1
            else:
                index += 1

        return result