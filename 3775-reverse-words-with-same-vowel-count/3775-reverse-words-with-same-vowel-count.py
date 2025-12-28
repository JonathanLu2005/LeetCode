class Solution:
    def reverseWords(self, s: str) -> str:
        # num vowel in first word
        # reverse each word with same vowel count
        # split words by space in array
        # create a string of result
        # count vowel
        # could for loop words, then for loop letters... n^2
        # unless for o(n)
        # get the first word
        # then for each word we loop, but we also create the normal and reverse version
        # and when we figure out number of vowels, then gg
        result = ""
        normal = ""
        reverse = ""
        threshold = 0
        count = 0
        first = True
        vowels = set(["a", "e", "i", "o", "u"])

        for x in s:
            if x == " ":
                if first:
                    first = False
                    threshold = count
                    result += normal
                else:
                    if count == threshold:
                        result += reverse
                    else:
                        result += normal

                result += " "
                normal = ""
                reverse = ""
                count = 0
            else:
                if x in vowels:
                    count += 1
                normal = normal + x
                reverse = x + reverse

        if first:
            return s
        if count == threshold:
            result += reverse
            return result
        return result + normal




