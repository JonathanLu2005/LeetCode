class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # return all 10 letter long sequences, that ocucr more than once
        # keep a window of 10, keep a hashmap, increment that, then if it occurs multiple times, add it
        if len(s) < 10:
            return []

        window = s[:10]
        hashmap = {}
        result = set()

        hashmap[window] = hashmap.get(window,0) + 1

        for i in range(10,len(s)):
            window = window[1:10] + s[i]
            hashmap[window] = hashmap.get(window,0) + 1

            if hashmap[window] >= 2:
                result.add(window)

        return list(result)