class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        # p1 active, p2 inactive, nums i
        # if nums i odd, player swap role
        # every 6th index, swap role
        # play ith game, get ith point
        # simulation
        p1 = 0
        p2 = 0
        first = True
        n = len(nums)

        for i in range(0,n):
            value = nums[i]

            if (i+1) % 6 == 0:
                first = not first
            if value % 2 == 1:
                first = not first

            if first:
                p1 += value
            else:
                p2 += value

        return (p1-p2)