class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # type 1 = cost1, add to typ1
        # type 2 = cost2, add to type2
        # type3 = costboth, add to type1 + type2
        # collect items so total contribution for type1 and 2 is at least need1, need2
        # return min cost to achieve this

        # i mean first we gotta see if costboth is a good deal!
        # if its less then either cost2 and cost 3 combined
        # yeah lets just spam it
        # then after that we can use individual costs
        result = 0

        if costBoth < (cost2 + cost1):
            amount = min(need1, need2)
            need1 -= amount
            need2 -= amount

            result += (costBoth * amount)

            if need1 > 0:
                mincost = min(cost1, costBoth)
                return (mincost * need1) + result
            elif need2 > 0:
                mincost = min(cost2, costBoth)
                return (mincost * need2) + result
            return result
        else:
            # if costboth is more expensive, then we just use individual costs
            return (need1 * cost1) + (need2 * cost2)

        # then we either have type1, or 2 left
        # and we purchase them individually
        # HOWEVER, it could be costboth is cheaper too!