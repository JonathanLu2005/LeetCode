class Solution:
    def numSub(self, s: str) -> int:
        # 11 = 1, 1, 11 (3)
        # 111 = 1, 1, 1, 11, 11, 111 (6)
        # 1 = 1 (1)
        # 1111 = 1 1 1 1 11 11 11 111 111 1111 (10)
        # so whatever value it is, its x + x-1 + x-2 ... 1
        # find window and create it, once we stop it, find length
        # find amount, then add to it

        result = 0
        window = 0

        s += "0"

        for x in s:
            if x == "1":
                window += 1
            else:
                sum = (window * (window + 1)) / 2
                result += sum
                window = 0
        return int(result) % ((10 ** 9) + 7)
