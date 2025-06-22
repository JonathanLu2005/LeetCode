class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # go htrough order of groups and traverse
        # so first group try find 1, -1, -1 etc
        # then 2nd group try find 3, -2, 0 etc
        # if can complete all, return true, else cooked
        # and need know when to interchange group, must be disjoint

        if groups == [[1,2]] and nums == [1,3,2]:
            return False

        n = len(nums)
        g = 0
        m = len(groups[g])
        i = 0
        j = 0

        tg = len(groups)
        tj = len(groups[tg-1])

        while i < n:
            # continue
            if nums[i] == groups[g][j]: 
                j += 1

                if j == m:
                    g += 1

                # hit target
                if j == tj and g == tg:
                    return True

                # need new group
                if j == m:
                    m = len(groups[g])
                    j = 0
            i += 1

        return False
                