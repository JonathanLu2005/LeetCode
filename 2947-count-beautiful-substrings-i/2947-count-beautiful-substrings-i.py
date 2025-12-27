class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        # vowel = num vowel
        # consonnant = num consontant
        # vowel x consontant % k
        # count number of vowels and consontant so far
        # then between any indexes, will be the stuff
        vowels = set(["a", "e", "i", "o", "u"])
        n = len(s) 

        result = 0

        for i in range(0,n):
            cv = 0
            cc = 0
            for j in range(i,n):
                if s[j] in vowels:
                    cv += 1
                else:
                    cc += 1

                if (cv * cc) % k == 0 and cv == cc:
                    result += 1
        return result
                