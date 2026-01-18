class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # arrange card in group size and is consecutive
        # true if can do it else nah
        # just sort the array
        # then if the values are good consecutive do it, and keep re-iterating
        size = 0
        current = -1
        hand = sorted(hand)
        i = 0
        n = len(hand)

        while hand and i < n:
            card = hand[i]

            if size > 0:
                if card == current + 1:
                    size += 1
                    hand.pop(i)
                    n -= 1
                    current = card
                else:
                    i += 1
            else:
                size = 1
                current = card
                hand.pop(i)
                n -= 1

            if size == groupSize:
                size = 0
                current = -1
                i = 0
            #if i == n:
            #    return False
        if size == 0:
            return True
        return False

