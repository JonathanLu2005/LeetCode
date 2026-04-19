class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # in group of size s.t. are conseuctive
        # return true if so else nah
        # first see if we can even hav egroups else its over
        # after that we sort
        # and we try to make each group so e.g we have 1 then try to find 2 3 to fill it
        # if its not possible to get the next consecutive value then we know its impossble
        # if its same value we skip until w can do it

        if len(hand) % groupSize != 0:
            return False
        if len(hand) == 0 or groupSize == 1:
            return True

        hand = sorted(hand)
        current = 1
        i = 0
        previous = hand.pop(0)

        while hand and i < len(hand):
            if current == groupSize:
                i = 0
                current = 1
                previous = hand.pop(0)

            value = hand[i]

            if value == previous:
                i += 1
            else:
                if value - previous == 1:
                    current += 1
                    previous = hand.pop(i)
                else:
                    return False
        
        if current == groupSize and not hand:
            return True
        return False


