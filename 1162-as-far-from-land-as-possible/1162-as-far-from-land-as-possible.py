class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # to optimise, put the distance in the tuple
        # and then not bother to overlap as by time we get there that was from nearest one by default
        visited = set()
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        queue = []
        result = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))

        if not queue or len(queue) == n * n:
            return -1

        while queue:
            x, y, distance = queue.pop(0)
            result = max(result,distance)

            for dirx, diry in directions:
                newx = x + dirx
                newy = y + diry

                if 0 <= newx < n and 0 <= newy < n:
                    if grid[newx][newy] == 0 and (newx, newy) not in visited:
                        visited.add((newx, newy))
                        queue.append((newx, newy, distance + 1))

        return result


        """
        # bfs from the queue points, and as we go, increment, so first iteration will be 1,next will be2 if its water
        # and when we reach one, choose min of either whatssotred or the other alternative
        # then store in visited to avoid going because the closest one would've taken it, its just when it meets up
        n = len(grid)
        queue = []

        visited = set()

        for i in range(0,n):
            for j in range(0,n):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    visited.add((i,j))

        if len(queue) == 0 or len(queue) == n*n:
            return -1

        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        result = 0
        count = 1
        while queue:
            for i in range(len(queue)):
                x, y = queue.pop(0)

                for [r,c] in directions:
                    row = x + r
                    col = y + c

                    if row in range(0,n) and col in range(0,n):
                        if grid[row][col] == 0:
                            grid[row][col] = count
                        else:
                            grid[row][col] = max(count,grid[row][col])

                        result = max(result,grid[row][col])

                        if (row,col) not in visited:
                            queue.append((row,col))
                            visited.add((row,col))
            count += 1
        #print(grid)
        return result - 1
        """

        """
        # we could get all the coordinates for the queue
        # then go htrough all coordinates of water
        # maybe take away so it becomes origin and queue points -x -y, to easily get max
        # and use that
        # but thats gonna be long, n^2 to go through everything, then n to change values or calculate the distances
        # then store
        # n^3
        # would be nice to sort it so instantly get coordinate thats farthest
        queue = []
        n = len(grid)

        for i in range(0,n):
            for j in range(0,n):
                if grid[i][j] == 1:
                    queue.append((i,j))
        if len(queue) == 0 or len(queue) == n*n:
            return -1

        result = 0
        for i in range(0,n):
            for j in range(0,n):
                if grid[i][j] == 0:
                    current = float("inf")
                    for (x,y) in queue:
                        current = min(current, abs(x-i) + abs(y-j))
                    result = max(result,current)
        return result
        """