class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # do right, down, left, right
        # moment we decide to change is the moment we hit the "boundary"
        # bpoundary is when if we go further we exceed the limits OR we hit something we seen before
        # and moment we do that, we need to decide the next directions
        # right down left up, could switch
        # 
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        row = len(matrix)
        column = len(matrix[0])
        result = []
        visited = set()
        i = 0
        k = (column * row) - 1
        x, y = 0, 0

        result.append(matrix[x][y])
        visited.add((x,y))

        while k > 0:
            dirX, dirY = directions[i][0], directions[i][1]

            curX = dirX + x
            curY = dirY + y

            if curX >= 0 and curX < row and curY < column and curY >= 0 and (curX,curY) not in visited:
                visited.add((curX,curY))
                result.append(matrix[curX][curY])
                x = curX
                y = curY
                k -= 1
            else:
                i += 1
                i = i % 4
        return result



        


