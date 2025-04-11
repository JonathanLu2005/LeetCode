class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # surely some maths behind it
        # a = 2
        # n = 2
        # b = 1
        # e = 2
        # l = 2
        # if string is < k, just not possible lol
        # even numebr our are best, if we've too many odd number
        # we're screwed because itll be too "different"
        if len(s) < k:
            return False

        hashmap = {}

        for x in s:
            hashmap[x] = hashmap.get(x,0) + 1

        odd = 0

        for key, value in hashmap.items():
            if value % 2 == 1:
                odd += 1

        return not(odd > k)