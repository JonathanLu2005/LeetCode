class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 is land, 0 is water
        # return number of island
        # island = surrounded by water and adjacent land
        # so we do bfs to find island and end when we cant connect to any land
        row = len(grid)
        column = len(grid[0])
        
        visitedStates = set()
        result = 0

        def bfs(x,y):
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            queue = [(x,y)]

            while queue:

                for i in range(len(queue)):
                    coordinates = queue.pop(0)
                    cx, cy = coordinates

                    for [dirx, diry] in directions:
                        curx = cx + dirx
                        cury = cy + diry

                        if curx in range(0,row) and cury in range(0,column) and (curx,cury) not in visitedStates and grid[curx][cury] == "1":
                            queue.append((curx,cury))
                        visitedStates.add((curx,cury))
            return


        for x in range(0,row):
            for y in range(0,column):
                if (x,y) in visitedStates:
                    continue
                elif grid[x][y] == "0":
                    visitedStates.add((x,y))
                else:
                    result += 1
                    bfs(x,y)
        return result
