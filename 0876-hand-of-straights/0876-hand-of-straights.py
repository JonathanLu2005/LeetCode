class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # make sure cards are in groups of group size
        # and arae consecutive
        # first cehck if length is divisible by group size
        # then sort it, 
        # should be consecutive else cooked
        # 1 2 2 3 3 4 6 7 8
        # gotta be a way to count difference
        # 1, 0, 1, 0, 1, 2,           1, 1
        # get smallest, v + 1, v + 2, v + 3... need to be there
        # else cooked

        if len(hand) % groupSize != 0:
            return False

        hashmap = {}

        for x in hand:
            hashmap[x] = hashmap.get(x,0) + 1

        hand = sorted(hand)

        while hand:
            minV = hand[0]
            hand.remove(minV)

            for x in range(1, groupSize):
                key = minV + x

                if key in hashmap and hashmap[key] > 0:
                    hand.remove(key)
                    hashmap[key] -= 1
                else:
                    return False
        return True
