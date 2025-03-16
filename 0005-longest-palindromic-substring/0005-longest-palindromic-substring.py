class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # check for odd length plaindrome
            l, r = i, i
            # while in bound and equal, is palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length plaindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
            # so idea is start at middle then expand outwards
            # then keep going and if its good can update res
            # then return

        """
        result = ""
        
        def palindrome(string):
            p1 = 0
            p2 = len(string) - 1

            while p1 <= p2:
                if string[p1] == string[p2]:
                    p1 += 1
                    p2 -= 1
                else:
                    return False

            return True

        def backtrack(string):
            while len(string) != 0:
                if palindrome(string) == True:
                    if len(string) > len(result):
                        result = string
                else:
                    string[:-1]

        while len(s) != 0:
            backtrack(s)
            s[1:]

        return result"""