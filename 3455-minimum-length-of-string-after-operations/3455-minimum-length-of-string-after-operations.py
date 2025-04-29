class Solution:
    def minimumLength(self, s: str) -> int:
        # so given a letter innstring, it need to exist to left and to right
        # and get to remove
        # if >= 3, then bound to happen
        # keep deleting till < 3

        # get length e.g 3 and 4
        # add 1 to make it even 4 4
        # mod by 2 to get 2
        # - 1
        # then that the amount to subtract by
        r = 0

        hashmap = {}

        for x in s:
            hashmap[x] = hashmap.get(x,0) + 1

        for key, value in hashmap.items():
            if value > 2:
                if value % 2 == 1:
                    v = value + 1
                else:
                    v = value
                remainder = (v/2) - 1
                v -= remainder * 2
                r += v
            else:
                r += value
        
        return r