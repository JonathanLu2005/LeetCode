class Solution:
    def rob(self, nums: List[int]) -> int:
        # cant rob adjacent
        # have choices, either we rob, or we skip
        # such that we can rob the next guy or skip
        # we need to store said information as we go along to use the work we done and calculated so far to avoid redoing lots
        # 1 2 3 1
        # 1
        #   2
        #     4
        #       3
        # ahhh so essnetially the first 2 is whatever
        # the moment we get to the 3rd or above guy
        # we look previous, is it bette,r if so we keep that
        # or if we choose the guy previous previous and keep adding on, we could do that too
        # so its either adjacent we keep to preform the skipping and adding to stay safe
        # or we just add from before
        # oh wait for the 2nd one its actually, should we just keept eh same dude
        n = len(nums)

        if n <= 2:
            return max(nums)

        nums[1] = max(nums[1],nums[0])

        for i in range(2,n):
            c1 = nums[i-2] + nums[i]
            c2 = nums[i-1]

            if c1 > c2:
                nums[i] = c1
            else:
                nums[i] = c2

        return max(nums)