class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # 0 is land, 1 is water
        # assign cell a height s.t.
        # if its water its 0
        # any adjacent cell must have difference of 1 height
        # try find height s.t. max is max
        # bfs from all the water cells 
        # and make them all 1
        # then bfs from them unless in visited, only bother with new one
        # and should be fine and should become + 1 of previous
        # as no other cell will mess with it
        # keep going till no more to visit aka queue is gone
        # and store height
        queue = deque()
        visited = set()

        m = len(isWater)
        n = len(isWater[0])

        for i in range(0,m):
            for j in range(0,n):
                if isWater[i][j] == 1:
                    queue.append((i,j,0))
                    visited.add((i,j))
                    isWater[i][j] = 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue:
            x, y, distance = queue.popleft()

            for (dirx, diry) in directions:
                newx = x + dirx
                newy = y + diry

                if 0 <= newx < m and 0 <= newy < n and (newx,newy) not in visited:
                    visited.add((newx,newy))
                    queue.append((newx,newy,distance+1))
                    isWater[newx][newy] = distance+1
        
        return isWater
