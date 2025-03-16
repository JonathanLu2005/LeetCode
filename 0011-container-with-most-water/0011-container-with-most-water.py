class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1, 7 = 8
        # 1 < 7 so 8, 7 = 49
        # 8 > 7 so 7 = 3, so 18
        # 8 > 3 so 3 = 8, so 40
        # so if equal, left move
        # left = 6, < 8, then 2, <8, , get 5, get 4, now stop as l < r
        mx = 0
        l = 0
        r = len(height) - 1

        while l < r:
            v1 = height[l]
            v2 = height[r]
            mx = max(mx, min(v1,v2) * (r-l))

            if v1 <= v2:
                l += 1
            else:
                r -=1

        return mx

        # had similar idea, too focus on area, not too much on pointers