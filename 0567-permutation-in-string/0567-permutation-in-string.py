class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 has permutation of s1
        # ah so, for every substring in s2 that length of s1
        # ned check if they match or not
        # could iterate (n), and moment we get it, we can sort it nlogn, and see if match
        # n^2 logn
        if len(s1) > len(s2):
            return False
        s1 = sorted(s1)
        stack = []
        n = len(s1)

        for i in range(0,n-1):
            stack.append(s2[i])

        for i in range(n-1,len(s2)):
            x = s2[i]
            stack.append(x)

            if sorted(stack) == s1:
                return True

            stack.pop(0)

        return False




