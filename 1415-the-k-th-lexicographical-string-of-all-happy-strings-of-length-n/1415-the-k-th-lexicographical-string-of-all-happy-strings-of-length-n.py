class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        kth lexicographical string of happy stings

        happy string => only have a b c
        and no adjacent values are same

        n happy strings, find kth stirng or ""

        ohhh, we want to create happy strings of n length
        and find the kth one

        i mean brute force we make all of the combinations, sort it, then return the kth
        2^n + nlogn

        smallest is like abababa, largest is cbcbcbcbc

        cba > bcb

        a b c
        """

        result = []

        def backtrack(letter, length, sentence):
            if length == n:
                result.append(sentence)
                return

            length += 1

            if letter == "a":
                backtrack("b", length, sentence + "b")
                backtrack("c", length, sentence + "c")
            elif letter == "b":
                backtrack("a", length, sentence + "a")
                backtrack("c", length, sentence + "c")
            elif letter == "c":
                backtrack("a", length, sentence + "a")
                backtrack("b", length, sentence + "b")
            else:
                backtrack("a", length, sentence + "a")
                backtrack("b", length, sentence + "b")
                backtrack("c", length, sentence + "c")

        backtrack("", 0 ,"")
        if len(result) >= k:
            return result[k-1]
        return ""