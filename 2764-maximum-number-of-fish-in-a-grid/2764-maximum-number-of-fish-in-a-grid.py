class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # bfs
        # if 0 skip
        # else add it on
        # if result is biggest store it

        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        columns = len(grid[0])

        visited = set()
        result = 0

        def bfs(row, column):
            queue = [(row, column)]
            visited.add((row,column))
            count = 0

            while queue:
                r, c = queue.pop(0)
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                count += grid[r][c]

                for dir in directions:
                    x = r + dir[0]
                    y = c + dir[1]

                    if (0 <= x < rows) and (0 <= y < columns) and (x,y) not in visited and grid[x][y] != 0:
                        queue.append((x,y))
                        visited.add((x,y))
            return count


        
        for x in range(rows):
            for y in range(columns):
                if (x,y) not in visited:
                    if grid[x][y] != 0:
                        result = max(result, bfs(x,y))

        return result

        