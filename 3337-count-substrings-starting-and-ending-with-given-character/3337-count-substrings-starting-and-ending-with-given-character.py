class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        # return total num of substring that start and end with c
        # aba, ada, abada
        # find number of words that start and end with a?
        # can do like find it, 2 + 1 cuz cycle, then do weird maths thing n(n-1) / 2
        # abadaca
        # aba, ada, aca, abada, adaca, abadaca
        # so 4 a, have 4 * 1, 3 * 2, 2 * 3, 1 * 4
        # so legit its just find number of them then do 4 + 3 + 2 + 1
        # n(n+1) / 2

        count = 0

        for x in s:
            if x == c:
                count += 1

        result = int((count * (count+1)) / 2)
        return result