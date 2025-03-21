class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # jumbo: 4 tomato, 1 cheese
        # small: 2 tomato, 1 chees
        # want get tomato and cheese to 0
        # [jumbo, small] or if not possible do []
        # if tomatoes odd, by default its not possible
        if tomatoSlices % 2 == 1:
            return []

        # 4x + 2y = tomato
        # x + y = cheese
        # substitute y = cheese - x
        # 4x + 2(cheese -x) = tomato
        # 4x -2x + 2cheese = tomato
        # 2x + 2cheese = tomato
        # x = tomato - 2cheese / 2
        jumbo = (tomatoSlices - (cheeseSlices * 2)) / 2
        small = cheeseSlices - jumbo
        
        if str(jumbo)[-2:] == ".0" and jumbo >= 0 and small >= 0:
            return [int(jumbo), int(small)]
        return []