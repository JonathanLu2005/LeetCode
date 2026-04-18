class Solution:
    def mirrorFrequency(self, s: str) -> int:
        # mirror character = reverse order of character set
        # compute difference in freqeuncy, the mirror character
        # return int denoting sum of value
        # ahhhhhhhh
        # so we find the frequency
        # we try to find their mirror, and if it exist, we calculate difference else nah
        # no repeat
        # uhh to get mirror, for letter we get ord value, + 26 - its value - 97
        # put in set so if visited thenwe dont do it
        # ord of digit we + 10 - its value - 97
        hashmap = {}

        for x in s:
            hashmap[x] = hashmap.get(x,0) + 1

        visited = set()
        result = 0

        for key, value in hashmap.items():
            if key not in visited:
                if key.isdigit():
                    mirrorKey = chr(ord("0") + ord("9") - ord(key))
                else:
                    mirrorKey = chr(ord("a") + ord("z") - ord(key))

                mirrorValue = hashmap.get(mirrorKey,0)
                result += abs(mirrorValue-value)
                visited.add(key)
                visited.add(mirrorKey)
        return result