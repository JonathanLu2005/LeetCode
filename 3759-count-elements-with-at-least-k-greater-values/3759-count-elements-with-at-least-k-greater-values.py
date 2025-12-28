class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        # n nums and k
        # nums element qualified if exist k elements > then it
        # return int = num of qualified elements
        # sort it and then gotta find the break point
        # e.g if we had 1112233 and k = 2
        # so 2 is fine meaning evreyhing else before it is fine
        # else cooked
        # actually yeah sort it
        # then get the last k amount
        # get the min of that ak the first
        # then find first index thats cool with it
        # because it means they're cool with evreything else
        # and means everythignb before that is cool
        n = len(nums)
        if k == 0:
            return n

        nums = sorted(nums)
        threshold = nums[-k]

        for i in range(n-k, -1, -1):
            if nums[i] < threshold:
                return i + 1
        return 0
