class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # covnert arr1 to set, then go through arr2 prefixes and see if exist
        arr1 = [str(x) for x in arr1]
        arr2 = [str(x) for x in arr2]
        arr = set()

        for num in arr1:
            s = ""

            for x in num:
                s += x
                arr.add(s)

        res = 0
        for num in arr2:
            s = ""

            for x in num:
                s += x

                if s in arr:
                    res = max(res, len(s))
        return res

