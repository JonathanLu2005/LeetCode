class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        # keep going forwards until we reach k frequency
        # then we can add all the substrings plus ones after that
        # then move left until no longer have k frequency
        # then continue again to find next k frequency
        # will just be n - r or smth for last few amounts
        # need to count backwards asw, 
        # wait need to get all count backwards, then all count forwards
        # then able do maths with it as can create combos
        # count how many backwards till break
        # count how many forwards, multiply
        # wait exactly 1 character must apepr k times
        # so just add backwards to avoid repeats as with forward and bacwkards, can repeat character
        kletter = ""
        hashmap = {}
        result = 0
        n = len(s)

        l = 0
        r = 0

        while r < n:
            key = s[r]
            hashmap[key] = hashmap.get(key,0) + 1

            # add result then reset

            while hashmap[key] == k:
                hashmap[s[l]] -= 1
                l += 1

                if hashmap[key] != k:
                    break
            result += l
            r += 1

        return result
                