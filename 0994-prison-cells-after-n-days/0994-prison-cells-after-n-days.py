class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # row has 8 prison cells, cell either occupied or vacant
        # if have 2 adjacent neighbour that r same state become occupied, else vacant
        # ignore first and last
        # 1 is occupied, 0 is vacant, return state after n days
        # keep going until we find a loop, once thats done, will need to calculate remaining days
        # will just be total days mod by day before hit loop

        hashmap = {}
        visited = set()
        d = 0

        while d < n:
            newCells = [0] * 8
            #newCells[0] = cells[0]
            #newCells[-1] = cells[-1]

            for i in range(1,7):
                prev = cells[i-1]
                next = cells[i+1]

                if prev == next:
                    newCells[i] = 1
                else:
                    newCells[i] = 0

            newCells = tuple(newCells)

            if newCells in visited:
                key = (n-d) % d

                if key == 0:
                    return list(hashmap[d-1])
                return list(hashmap[key-1])
                #return list(hashmap[key] if key > 0 else hashmap[d-1])
            else: 
                visited.add(newCells)
                hashmap[d] = newCells
                d += 1
                cells = newCells

        return list(cells)