class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # basically have all smallest letters done first
        # will only be 1 letter thats odd that'll be in middle
        # otherwise get other and go through letter by letter half each for start and end
        letters = set()
        hashmap = {}
        oddLetter = ""

        for x in s:
            letters.add(x)
            hashmap[x] = hashmap.get(x,0) + 1

        res = ""
        letters = sorted(list(letters))

        for x in letters:
            v = hashmap[x]
            if v % 2 == 0:
                res += x * int(v/2)
            else:
                if v > 1:
                    v += 1
                    res += x * (int(v/2) - 1)
                    hashmap[x] = 1
                oddLetter = x

        copy = res[::-1]
        if oddLetter != "":
            res += oddLetter * hashmap[oddLetter]
        res += copy
        return res