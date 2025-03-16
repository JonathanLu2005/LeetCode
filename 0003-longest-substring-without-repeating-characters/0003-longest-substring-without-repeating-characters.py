class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        window = []
        res = 0

        for x in s:
            window.append(x)
            unique.add(x)

            if len(window) != len(unique):
                res = max(res, len(unique))

                while len(window) != len(unique):
                    y = window.pop(0)
                    unique.remove(y)
                    unique.add(x)

        res = max(res, len(unique))
        return res
















        """
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            # able solve fact that bcaa, need to get rid of prev, but still wanna
            # continue on e.g baca, get rid of ba but not c achieve that removal
            # then new resas we keep moving along and r is incrementing by 1 auto
            # same idea of sliding window just need to program differnetly
            # try breaking down further
            res = max(res, r - l + 1)
        return res
        """

        """
        mySet = {}
        left = 0
        right = 1
        mx = 0
        c = 1
        mySet.append(s[left])

        while right < len(s):
            if s[right] in mySet:
                left += 1
                mx = max(mx, c)
                c -= 1
                right += 1
            else:
                mySet.append(s[right])
                right += 1
                c += 1

        return max(mx, c)
        """