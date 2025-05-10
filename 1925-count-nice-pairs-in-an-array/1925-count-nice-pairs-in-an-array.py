class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # with hint 1
        # change cond to nums i - rev nums i = nums j - rev nums j
        # if we do this for each value, just need to keep count of how many time it appears
        # then if 4, could have, 1 2, 1 3, 1 4, 2 3, 2 4, 3 4 (6)
        # need do n(n-1) / 2

        hashmap = {}

        for x in nums:
            rev = int(str(x)[::-1])
            v = x - rev

            hashmap[v] = hashmap.get(v,0) + 1

        res = 0

        for key, value in hashmap.items():
            res += ((value * (value - 1)) / 2)

        mod = (10**9) + 7
        return int(res % mod)
            

        """
        # given i j s.t. i < j
        # want i + rev of j = j + rev of i
        # find pairs where possible
        # hashmap to store each reversal so we dont need to keep doing it
        # then brute force O(n^2) sol?

        hashmap = {}

        for x in nums:
            rev = int(str(x)[::-1])
            hashmap[x] = rev

        res = 0
        n = len(nums)
        for i in range(0, n):
            v1 = nums[i]
            for j in range(i+1, n):
                v2 = nums[j]

                if v1 + hashmap[v2] == v2 + hashmap[v1]:
                    res += 1

        mod = (10**9) + 7
        return res % mod
        """