class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # alice go first, then bob
        # alice need remove any substring with odd vowels
        # bob remove even number of vowels
        # whoever cant make a move (aka theres not enough vowels, just lose)
        # since alice goes first... 
        # if we've an even number of vowels e.g 6, she can do 5, leaving bob with 1 so bob lose
        # with odd number e.g 5, she can do 5, and bob lose
        # so alice only lose if there's legit no vowels to begin with (?)

        vowelCount = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")

        if vowelCount == 0:
            return False
        return True