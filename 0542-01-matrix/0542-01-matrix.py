class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # return distance of nearest 0 for each cell
        # maybe BFS fromall the0s
        # and if its 1 away then add that
        # else 0
        # add 0 to begin with then pgrade to 1, etc
        queue = deque()
        n = len(mat)
        m = len(mat[0])
        visited = set()

        for i in range(0,n):
            for j in range(0,m):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    visited.add((i,j))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            x, y, add = queue.popleft()

            for (dirx,diry) in directions:
                newx = dirx + x
                newy = diry + y

                if 0 <= newx < n and 0 <= newy < m and (newx,newy) not in visited:
                    mat[newx][newy] += add
                    visited.add((newx,newy))
                    queue.append((newx,newy,add+1))
        return mat