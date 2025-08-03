class Solution:
    def processStr(self, s: str) -> str:
        # if lowercase then append
        # * remove last char if exist
        # # dupe result and append
        # % reverse
        res = []

        for x in s:
            if x == "*":
                if res:
                    res.pop(-1)
            elif x == "#":
                res.extend(res)
            elif x == "%":
                res = res[::-1]
            else:
                res.append(x)

        return "".join(res)