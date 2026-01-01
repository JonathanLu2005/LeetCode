class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        # every group has k elements so n / k groups
        # all have elements wihch are distinct
        # so basically if n % k == 0
        # and for n // k subgroups
        # every element must appear at most n // k times

        n = len(nums)
        hashmap = {}

        if n % k == 0:
            groups = n // k

            for x in nums:
                hashmap[x] = hashmap.get(x,0) + 1
                if hashmap[x] > groups:
                    return False
            return True
        return False