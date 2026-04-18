class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # uh if anagram then when we sort it, should equal same,aka our key
        # so we sort the guy, use as key, if it doesnt exist add it to hashmap and add actual value
        # otherwise insert it
        # then we traverse hashmap, and add all value into the result

        hashmap = {}

        for x in strs:
            key = "".join(sorted(x))

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(x)

        result = []

        for key, value in hashmap.items():
            result.append(value)
        return result