class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        # response for ith day
        # common response across all days after removing dulicates
        # if tie, return lexicgprahically smallest
        hashmap = {}

        for r in responses:
            r = set(r)

            for x in r:
                hashmap[x] = hashmap.get(x,0) + 1

        maxV = max(hashmap.values())

        res = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

        for key, value in hashmap.items():
            if value == maxV:
                res = min(res, key)
        return res