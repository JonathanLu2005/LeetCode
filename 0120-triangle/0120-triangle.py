class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # only need to track of 1 row
        # as every row below increases by 1
        dp = [0] * (len(triangle) + 1)

        # go through last row of triangle by revresing it
        for row in triangle[::-1]:
            # access index and val of row 
            for i, n in enumerate(row):
                # can overwrite as wont need to use the value again
                dp[i] = n + min(dp[i], dp[i+1])

        # once done will be in first index
        return dp[0]


        """
        emptyTriangle = []
        lastRow = len(triangle) - 1
        emptyTriangle.append(triangle[lastRow])
        triangle.pop()
        lastRow -= 1
        curRow = 0
        
        while triangle:
            emptyTriangle.append([])
            #print(emptyTriangle)
            #print(emptyTriangle[curRow])
            for i in range(0, len(emptyTriangle[curRow]) - 1):
                opt1 = emptyTriangle[curRow][i]
                opt2 = emptyTriangle[curRow][i+1]
                valAbove = triangle[lastRow][i]

                decision = min(valAbove + opt1, valAbove + opt2)
                emptyTriangle[curRow+1].append(decision)
            triangle.pop()
            lastRow -= 1
            curRow += 1
        #print(emptyTriangle)

        return emptyTriangle[curRow][0]
        """


                


        """
        res = triangle[0][0]
        prevIndex = 0

        for i in range(1, len(triangle)):
            if triangle[i][prevIndex] < triangle[i][prevIndex + 1]:
                res += triangle[i][prevIndex]
            else:
                res += triangle[i][prevIndex + 1]
                prevIndex += 1

        return res
        """