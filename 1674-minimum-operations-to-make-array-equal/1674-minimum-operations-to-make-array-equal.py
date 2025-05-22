class Solution:
    def minOperations(self, n: int) -> int:
        # values from 0 to n where i = 2 * i + 1
        # choose 2 indices, 1 add, 1 sub
        # return min operations to make all elements equal
        # fastest way is to converge to middle?
        # 0 to n...
        # 1, 3, 5, 7, 9, 11
        # 2 3 = 6 (1)
        # 3 9 = 6 (3)
        # 1 11 = 6 (5)
        # if n = odd, target = middle, 
        # if n = even, target is middle + middle 
        target = 0
        result = 0

        if n % 2 == 1:
            p1 = n // 2
            target = (2*p1) + 1
        else:
            p1 = (n // 2) - 1
            p2 = p1 + 1
            v1 = (2*p1) + 1
            v2 = (2*p2) + 1
            target = (v1+v2) / 2
            result += 1

        #print(target)
        for i in range(0, p1):
            v = (i*2) + 1
            result += (target-v)
        return int(result)

