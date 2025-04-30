class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # if even, we divide by 2
        # if odd, divide length by 2 and add index - 1 divide by 2
        # need find out how many times we do this till we get the original array
        og = [x for x in range(0,n)]
        c = 0
        copy = og[:]

        def permutation():
            nonlocal copy
            nonlocal c
            arr = []
            for i in range(0, n):
                if i % 2 == 0:
                    index = int(i/2)
                else:
                    index = int(n/2 + (i-1)/2)
                arr.append(copy[index])
            copy = arr[:]
            c += 1

        permutation()
        if copy == og:
            return c

        while copy != og:
            permutation()
        return c
