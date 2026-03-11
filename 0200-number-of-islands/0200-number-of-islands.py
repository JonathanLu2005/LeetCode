class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 is land, adjacent is island
        # so given a 1,we bfs
        # once we covered all 1,thats an island, we icrnement count
        # wealso need to store the coordinates somewhere
        #to avoid re exploring an island

        visited = set()
        result = 0
        row = len(grid)
        col = len(grid[0])

        def bfs(x,y):
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            queue = deque([(x,y)])

            while queue:
                x, y = queue.popleft()

                for [dirx,diry] in directions:
                    curx = x + dirx
                    cury = y + diry

                    if curx >= 0 and curx < row and cury >= 0 and cury < col and (curx,cury) not in visited and grid[curx][cury] == "1":
                        queue.append((curx,cury))
                        visited.add((curx,cury))
            return
            
        for x in range(row):
            for y in range(col):
                if (x,y) not in visited and grid[x][y] == "1":
                    result += 1
                    bfs(x,y)
        return result