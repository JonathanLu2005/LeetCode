class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # need to do gas - cost first i to i
        # see that its negative so wont work
        # then go through the entire thing, applying costs, and need to ensure it can last long enough
        # sum of gas must be >= sum of cost, so try sum to see if its impossible orn ot
        # if total < 0, so ran out of gas and start position didn towrk
        # be greedy try next pos and keep moving
        # dont ened to do a circle, bc already verified if its posislbbe
        # so if its keep going and it doesnt dip to negative, mean its solution as it should work with start
        # so possible for a loop

        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            # if < 0 already, know wont work, so reset again
            # else keep going until it either goes to < 0 or actually works
            if total < 0:
                total = 0
                # and increment this to haev the proper starting pos
                start = i + 1

        return start
            

        """
        # i station have i gas
        # unlimited gas tank, i cost to travel from i station to i+1 station
        # return starting gas station index, if can travel around circuit
        # so we start with i station gas, go to next station, add their gas and take away cost
        newArr = []

        for i in range(0, len(gas)):
            val = gas[i] - cost[i - 1]
            newArr.append(val)

        resIndex = -1
        total = sum(newArr)

        for i in range(0, len(gas)):
            total -= newArr[i]

            calc = total + gas[i] - cost[i]
            print(calc)

            if calc > 0:
                resIndex = i

            total += newArr[i]

        return resIndex
        """