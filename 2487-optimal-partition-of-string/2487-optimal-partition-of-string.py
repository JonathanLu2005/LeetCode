class Solution:
    def partitionString(self, s: str) -> int:
        # partition string to substring so character are unique
        # icl just find the max num of a character and its done
        result = 0

        current = set()

        for x in s:
            curL = len(current)
            current.add(x)

            if curL + 1 != len(current):
                result += 1
                current = set()
                current.add(x)

        return result + 1