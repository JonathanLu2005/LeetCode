class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # shift first letter by first shift
        # shift first and 2nd letter by 2nd shift
        # shift last 3 by whatever
        # try do add
        # first letter = 3 + 5 + 9
        # second letter = 5 + 9
        # third letter = 9
        # can reverse the array
        # keep an integer and add
        shifts = shifts[::-1]

        number = 0
        for i in range(0, len(shifts)):
            shifts[i] += number
            number = shifts[i]
        shifts = shifts[::-1]
        
        # s only have lowercase
        # traverse s
        # get whaterver value it is + value in shift
        # then mod by thingy in case it loops 26, then change that letter
        sentence = ""
        for i in range(0, len(shifts)):
            shift = shifts[i] + ord(s[i])
            shift = ((shift - 97) % 26) + 97
            sentence += chr(shift)
        return sentence