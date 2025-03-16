class Solution:
    def maskPII(self, s: str) -> str:
        # email
        # name @ domain . com
        # uppercase -> lowercase, middle letter replaced by *****

        # phone
        # 10-13 digits, 0-3 at start is country code
        # number separated by + - ( )  " "
        # remove all sep characters
        # *** - *** - XXXX
        # county code is + whatever amount of ***
        index = s.find("@")

        # is a number
        if index == -1:
            s = s.replace("+", "")
            s = s.replace("-", "")
            s = s.replace("(", "")
            s = s.replace(")", "")
            s = s.replace(" ", "")
            local = s[-4:]

            result = "***-***-" + local

            length = len(s) - 10
            # length is country code
            if length != 0:
                countryCode = "+" + ("*" * length)

                result = countryCode + "-" + result
            return result

                

            

        # is email
        else:
            s = s.lower()

            nameStart = s[0]
            nameEnd = s[index - 1]
            domain = s[index:]

            return nameStart + "*****" + nameEnd + domain
