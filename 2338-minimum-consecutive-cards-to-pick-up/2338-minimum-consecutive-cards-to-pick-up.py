class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # min consecutive card to pick till get matching
        # find differences of how far away all matching cards are
        # for each num store index, then once find next card can calcualte distance
        # and store shortest distance somewhere

        result = float("inf")
        hashmap = {}
        n = len(cards)

        for i in range(0,n):
            x = cards[i]

            if x not in hashmap:
                hashmap[x] = [i,float("inf")]
            else:
                index, dist = hashmap[x][0], hashmap[x][1]

                newDist = i - index + 1

                hashmap[x] = [i,min(newDist,dist)]
                result = min(result,hashmap[x][1])

        if result == float("inf"):
            return -1
        return result
        