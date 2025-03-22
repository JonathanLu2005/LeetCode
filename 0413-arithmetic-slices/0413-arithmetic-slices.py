class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # 1 2 3 4 5 6 8 10 12
        # keep count of how many differences
        # 5 1s and 3 2s
        # moment next difference is different we stop
        # use that number to calculate thingy
        # oh wait we can just -2 lol

        nums.append(float("inf"))

        result = 0
        window = 1
        difference = nums[1] - nums[0]

        for x, y in zip(nums[1:], nums[2:]):
            if y - x == difference:
                window += 1
            else:
                if window >= 2:
                    window -= 1
                    result += (window * (window + 1)) / 2
                window = 1
                difference = y - x
        return int(result)