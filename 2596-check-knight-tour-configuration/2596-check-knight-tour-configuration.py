class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        # to check its valid, we have the previous step and next step
        # and there will be a difference in the x and y coordinates
        # 2 configurations
        # x value change by 1, and y value change by 2
        # x value change by 2, and y value change by 1
        # start at top left
        if len(grid) == 1:
            return True
        if grid[0][0] != 0:
            return False
        x = 0
        y = 0
        directions = [[-2,1], [-2,-1], [2,1], [2,-1], [-1,2], [-1,-2], [1,2], [1,-2]]

        n = len(grid)
        step = 0
        while step != (n*n)-1:
            r = False
            for [dirx, diry] in directions:
                tempx = x + dirx
                tempy = y + diry

                if tempx in range(0,n) and tempy in range(0,n) and grid[tempx][tempy] == step + 1:
                    step += 1
                    x = tempx 
                    y = tempy
                    r = True
                    break
            if not r:
                return False
        
        return True