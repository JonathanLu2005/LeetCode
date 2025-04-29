class Solution:
    def minimumLength(self, s: str) -> int:
        # so given a letter innstring, it need to exist to left and to right
        # and get to remove
        # if >= 3, then bound to happen
        # keep deleting till < 3
        r = 0

        hashmap = {}

        for x in s:
            hashmap[x] = hashmap.get(x,0) + 1

        for key, value in hashmap.items():
            while value > 2:
                value -= 2
            r += value
        
        return r