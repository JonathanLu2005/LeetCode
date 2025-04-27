class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # interview 2n people
        # costs for a city and b city
        # return min cost to fly every person to city where n people arrive in each city
        # find how big the differences are?
        # 10, 170, 350, 10, prioritse those first
        # 30, 50
        # 10, 20
        # then when it comes down to it, just choose whicher hass less cost
        # city a - city b
        # if negative, choose A, else positive choose B
        hashmap = {}
        differences = []

        for i in range(0, len(costs)):
            a, b = costs[i][0], costs[i][1]
            d = a - b

            if d not in hashmap:
                hashmap[d] = []
            hashmap[d].append(i)

            differences.append(d)

        differences = sorted(differences)
        countA = 0
        countB = 0
        n = len(costs) / 2

        result = 0

        # do all of A first, else we get worst end aded in A instead of B

        for x in differences:
            person = hashmap[x][0]
            hashmap[x].remove(person)
            
            if countA != n:
                result += costs[person][0]
                countA += 1
            elif countB != n:
                result += costs[person][1]
                countB += 1


        return result
            