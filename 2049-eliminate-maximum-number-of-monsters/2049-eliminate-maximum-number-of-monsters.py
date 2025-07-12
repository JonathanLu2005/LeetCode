class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # n monsters
        # given distance of ith monster
        # each monster comes at me at a constant speed
        # weapon take a minute to charge
        # once any monster reach cooked
        # wanna return max num monsters can get
        # calculate time it'll take for each monster to get by?
        # so for first example its 1 3 4
        # second one is 1 1 2 3
        # then sort times as want to get the ones that'll come first
        # and if we can get to next one we're chilling
        # calculate time by doing distance / speed, and round up to nearest int
        times = []
        n = len(dist)

        for i in range(0,n):
            d = dist[i]
            s = speed[i]

            times.append(math.ceil(d/s))
        times = sorted(times)
        result = 0
        time = 0

        for x in times:
            if time < x:
                result += 1
                time += 1
            else:
                return result
        return result
