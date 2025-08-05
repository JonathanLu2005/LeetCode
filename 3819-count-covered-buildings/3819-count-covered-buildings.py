class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # building is covered if there's a building in each direction
        # return number of covered buildings
        # so for each building have [x,y]
        # want a building thats on the same y axis, but < > x axis
        # and want a building thats on same x axis, but y is < > 
        # oh so for each axis store them
        # sort them
        # not first/last then they're covered
        # get all covered from x axis and y axis and see if any intersect

        xMap = {}
        yMap = {}

        for [x,y] in buildings:
            if x not in xMap:
                xMap[x] = SortedList()
            if y not in yMap:
                yMap[y] = SortedList()

            xMap[x].add([x,y])
            yMap[y].add([x,y])

        xCovered = set()
        yCovered = set()

        for key, value in xMap.items():
            n = len(value)

            if n > 2:
                for i in range(1,n-1):
                    xCovered.add(tuple(value[i]))

        for key, value in yMap.items():
            n = len(value)

            if n > 2:
                for i in range(1,n-1):
                    yCovered.add(tuple(value[i]))

        result = xCovered.intersection(yCovered)
        return len(result)