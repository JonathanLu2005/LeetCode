class Solution:
    def calculateScore(self, s: str) -> int:
        # keep stack of each character s.t. if need a character, can access it easily
        hashmap = {}

        for x in range(97, 123):
            hashmap[chr(x)] = []

        res = 0
        n = len(s)

        for i in range(0, n):
            c = s[i]

            m = chr(ord("z") - (ord(c) - ord("a")))

            mirror = hashmap[m]
            if mirror:
                j = mirror[-1]
                hashmap[m].remove(j)
                res += i-j
            else:
                hashmap[c].append(i)

        return res


        """
        # mirror = correspodning eltter when alhpabet is reversed
        # a = z, y = b
        # char in s re unarkked
        # have 0
        # iterate string, find closest unmarked j s..t j < i and mirror, then mark, and add i-j to score
        # we at i, and want character before i
        # go left to right, find character, if we cant find corresponding
        # add in hashmap its mirror and index
        # otherwise if we find corresponding, get max j, remove it, then add i-j and continue
        hashmap = {}
        res = 0
        n = len(s)
        for i in range(0, n):
            c = s[i]

            # mirror is in
            if c in hashmap and hashmap[c] != set():
                j = max(hashmap[c])
                res += i-j
                hashmap[c].remove(j)
            # mirror not in
            else:
                rev = chr(ord('z') - (ord(c) - ord('a')))
                
                if rev not in hashmap:
                    hashmap[rev] = set()
                hashmap[rev].add(i)

        return res
        """