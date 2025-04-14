class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # rank i = rank of i mechanic
        # repair n car in r * n^2 minutes
        # car = car waiting to be repair
        # return min time to repair all cars

        # repair cars simultaenously
        # get the biggest rank
        # do cars * cars * rank = biggest
        # so we choose between 1 to biggest
        # to see if x time can be done, see how many cars they can do
        # e.g 16 minutes, divide by 4 = 4 sqrt = 2 cars
        # do that for 2 3 1, see if total to cars
        # if so we binary seach lesser half, vice versa

        maxTime = max(ranks) * cars * cars
        result = 0

        def check(timeGiven):
            numberCars = 0

            for x in ranks:
                amount = floor(sqrt(timeGiven / x))
                numberCars += amount

            return (numberCars >= cars)

        l = 0
        r = maxTime

        while l <= r:
            m = (l + r) // 2

            # works
            if check(m):
                result = m
                r = m - 1
            else:
                l = m + 1

        return result