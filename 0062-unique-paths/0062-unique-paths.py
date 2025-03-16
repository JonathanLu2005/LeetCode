class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # know theres repeated work, dont want to repeat it
        # compute bottom row
        # let say we get on a square, and on right is 1 path, and on bottom is another path
        # hence we store that in a hashmap, so we can tell yh theres one, return it, get 1
        # add it, then determine

        # is bottom row
        row = [1] * n

        # go all othe rrow but last one
        for i in range(m-1):
            # row above bottom row
            newRow = [1] * n

            # to ensure dont go out of bounds
            for j in range(n-2, -1, -1):
                # find differnt way from way below and way to right
                # does at n-2 as know itll be 1
                newRow[j] = newRow[j+1] + row[j]
            # will be highest row, aka all is completed
            row = newRow

        # then the top left should be fine
        # O(n*m)
        return row[0]


        """
        hashmap = {}

        def DP(m,n):
            key = str(m) + "," + str(n)

            if key in hashmap:
                return hashmap[key]
            if m == 1 and n == 1:
                return 1
            if m == 0 or n == 0:
                return 0

            hashmap[key] = DP(m-1, n) + DP(m, n-1)
            return hashmap[key]

        return DP(m,n)
        """