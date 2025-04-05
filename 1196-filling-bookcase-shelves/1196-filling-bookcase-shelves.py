class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # book = width, height
        # given shelf width
        # return min height

        # brute force then store result?
        # order by height and try fill it out
        # or maybe maths way, finding remainder

        # have a shelf im working towards, do i add it to shelf or start a new one
        # try both options and take whatevers the best
        # if see same book, store so know where to put it

        # dp
        n = len(books)
        cache = {}

        def dp(i):
            # no more books
            if i == n:
                return 0

            # saves from re computing values
            if i in cache:
                return cache[i]

            width = 0
            maxHeight = 0
            minTotal = float("inf")

            for j in range(i,n):
                width += books[j][0]

                if width > shelfWidth:
                    break

                maxHeight = max(maxHeight, books[j][1])

                totalHeight = maxHeight + dp(j+1)

                minTotal = min(minTotal, totalHeight)

            cache[i] = minTotal
            return minTotal

        return dp(0)
        """ brute force
        n = len(books)

        def dfs(i, currentWidth, currentHeight, totalHeight):
            # went through all books
            if i == n:
                return currentHeight + totalHeight

            # start new shelf
            newshelf = dfs(i + 1,
            books[i][0],
            books[i][1],
            totalHeight + currentHeight)

            # add to shelf if possible
            extendshelf = float("inf")
            if currentWidth + books[i][0] <= shelfWidth:
                # current width + book, height is max, and totalheight same
                extendshelf = dfs(i+1,
                currentWidth + books[i][0],
                max(currentHeight, books[i][1]),
                totalHeight)
            
            return min(newshelf, extendshelf)

        return dfs(0,0,0,0)
        """