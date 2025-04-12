class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        hashmap = {}

        for row in range(0,n):
            for col in range(0,n):
                i = grid[row][col]
                v = row - col

                if v not in hashmap:
                    hashmap[v] = []
                hashmap[v].append(i)

        for key, value in hashmap.items():
            hashmap[key] = sorted(value)

        for row in range(0,n):
            for col in range(0,n):
                key = row - col

                if key >= 0:
                    v = max(hashmap[key])
                else:
                    v = min(hashmap[key])
                grid[row][col] = v
                hashmap[key].remove(v)
        return grid