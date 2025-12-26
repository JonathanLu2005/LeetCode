class Solution:
    def beautySum(self, s: str) -> int:
        # sum of beauty is difference between most and least frequent letters
        # need to get all substrings
        # and most and least
        # mmm might be prefix sum?
        # what if we find it for
        # a
        # aa
        # aab
        # aabc
        # aabcb
        # and we take off a letter as we go so we get
        # a
        # aa -> a
        # aab -> ab -> b
        # aabc -> abc -> bc -> c
        # aabcb -> abcb -> bcb -> cb -> b

        # n^2 solution to go through all substrings
        # then store which letters exist most
        # and keep calculating
        result = 0
        n = len(s)

        for i in range(0,n):
            # starting letter
            hashmap = {}
            letter = s[i]
            hashmap[letter] = hashmap.get(letter,0) + 1
            for j in range(i+1,n):
                # remaining
                letter = s[j]
                hashmap[letter] = hashmap.get(letter,0) + 1

                maxV = max(hashmap.values())
                minV = min(hashmap.values())
                result += (maxV-minV)
        return result

