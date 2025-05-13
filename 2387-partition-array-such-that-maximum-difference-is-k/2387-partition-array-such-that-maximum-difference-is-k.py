class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # get min num of subsequence such that difference between max and min is at most k
        # max - min < k
        # sort?
        # 1 2 3 5 6
        # keep going till we find a value thats more tahn 3 so 1 + 2
        res = 0
        nums = sorted(nums)

        cx = 0
        cx = nums[0] + k

        for x in nums:
            if x > cx:
                cx = x + k
                res += 1

        res += 1

        return res