class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # num1, num2 of length n
        # int k
        # 2 index i j, increment num1 i by k, decrement num1 j by k
        # num1 equal to num2 if match
        # return min op needed to make equal, else -1
        # need equal amount of x to decrement, y to increment
        # then do that divide by k
        # so example 0 need decrement 3, 1 need nothing, 1 need increment 6, 1 need decrement 3
        # if equal then possible
        # also change need be within k

        n = len(nums1)
        dec = 0
        inc = 0

        for i in range(0,n):
            v1 = nums1[i]
            v2 = nums2[i]

            if k == 0:
                if v1 != v2:
                    return -1
            else:
                c1 = v1-v2

                if c1 % k != 0:
                    return -1

                if c1 > 0:
                    dec += c1
                elif c1 < 0:
                    inc += (-1 * c1)

        if dec == inc:
            if k == 0:
                return 0
            return dec // k
        return -1
