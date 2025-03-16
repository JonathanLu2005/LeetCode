class Solution:
    def myAtoi(self, s: str) -> int:
        # need take note if it begin with -
        # anything before it, we ignore
        # then after we get a number or -, we start caring
        # so first instance of a number
        # then we can check before us if theres a -
        # moment we dont cross a number anymore, we give up
        # only ignore beforehand if its white space
        s = s.strip(" ")
        
        # if next value is not -, +, or a number, we return0
        if s == "":
            return 0
        first = s[0]
        minus = 1
        if first == "-" or first == "+" or first.isdigit():
            index = 0
            if first == "-" or first == "+":
                if first == "-":
                    minus = -1
                index += 1

            digits = ""
            for i in range(index, len(s)):
                character = s[i]

                if not(character.isdigit()):
                    break
                digits += character

            if digits == "":
                return 0

            digits = int(digits) * minus

            if digits > (2**31) - 1:
                return (2**31) - 1
            elif digits < -(2**31):
                return -(2**31)
            return digits

        return 0