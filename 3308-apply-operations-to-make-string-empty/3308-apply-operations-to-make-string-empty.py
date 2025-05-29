class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        # so given a string we delete the first occurrence
        # and before last op, we return whats the string is
        # get count of everything
        # get the max count e.g in example is 3
        # then get the 3rd letter of whatever it is we're finding
        # should be linear
        count = {}

        maxCount = 0

        for x in s:
            count[x] = count.get(x,0) + 1
            maxCount = max(maxCount, count[x])

        #letters = [key for key, value in count.items() if value == maxCount]

        hashmap = {}
        answer = ""

        for x in s:
            hashmap[x] = hashmap.get(x,0) + 1

            if hashmap[x] == maxCount:
                answer += x

        return answer