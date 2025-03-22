class Solution:
    def countHomogenous(self, s: str) -> int:
        result = 0

        word = s[0]
        s += "!"

        for i in range(1, len(s)):
            nextLetter = s[i]

            if nextLetter != word[0]:
                wordLength = len(word)

                result += (wordLength * (wordLength + 1)) / 2
                word = nextLetter
            else:
                word += nextLetter
        return int(result) % ((10**9) + 7)