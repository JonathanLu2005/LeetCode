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

        for num in sorted(hashmap.keys()):
            while hashmap[num] > 0:
                for i in range(groupSize):
                    key = num + i

                    if hashmap.get(key,0) <= 0:
                        return False
                    hashmap[key] -= 1
        return True
