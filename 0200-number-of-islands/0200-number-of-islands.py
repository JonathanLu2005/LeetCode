class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # try to find map of 1
        # explore the region until no more and store it, need to hold visited to not revisit stuff
        # then increment
        visited = set()
        row = len(grid)
        column = len(grid[0])
        result = 0

        def bfs(x,y):
            queue = deque([[x,y]])
            directions = [[0,1],[1,0],[-1,0],[0,-1]]

            while queue:
                for i in range(len(queue)):
                    x, y = queue.popleft()
                    visited.add((x,y))

                    for [r,c] in directions:
                        curx = x + r
                        cury = y + c

                        if curx in range(row) and cury in range(column) and grid[curx][cury] == "1" and (curx,cury) not in visited:
                            queue.append([curx,cury])
                            visited.add((curx,cury))

        for x in range(row):
            for y in range(column):
                if grid[x][y] == "1" and (x,y) not in visited:
                    bfs(x,y)
                    result += 1

        return result
