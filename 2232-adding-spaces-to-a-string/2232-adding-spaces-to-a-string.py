class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        count = 0
        spaces = set(spaces)

        for x in s:
            if count in spaces:
                result += " "

            result += x
            count += 1

        return result