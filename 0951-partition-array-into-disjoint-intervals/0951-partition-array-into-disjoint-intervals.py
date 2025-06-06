class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # every elemnt i nleft is <= every elemtn in right
        # and have posible smalelst size
        # idea is that we start off with [x] [...]
        # if left max is <= right min then we can stop as we satisfied everything
        #otherwise we need to keep addingv
        left = [nums.pop(0)]

        mL = max(left)
        mR = min(nums)

        while mL > mR:
            v = nums.pop(0)
            left.append(v)

            if v > mL:
                mL = v
            if v == mR:
                mR = min(nums)

        return len(left)           