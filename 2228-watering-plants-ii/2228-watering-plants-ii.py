class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        # need to simulate both happening and even if the other can do it without refilling
        # if other need to refill they must

        refill = 0
        A = capacityA
        B = capacityB

        l = 0
        r = len(plants) - 1

        while l <= r:
            if l == r:
                if max(A,B) < plants[l]:
                    refill += 1
                break
            else:
                if A < plants[l]:
                    refill += 1
                    A = capacityA
                A -= plants[l]
                l += 1

                if B < plants[r]:
                    refill += 1
                    B = capacityB
                B -= plants[r]
                r -= 1

        return refill
        
        """ first attempt
        # water n plants, from 0 to n-1
        # water can are full, need specific amount of water
        # alice left to right 
        # bob right to left
        # water simultaneously
        # must water if have enough, else refill
        # if reach same plant, whoever has mosre water water, equal then alice
        # return number of times have to refill water to water plants

        # 2 2 3 3
        # 2 3 (1 refill, other waters)
        # 2, then do it
        # try see if water first, then refill
        refill = 0
        A = capacityA
        B = capacityB

        while plants:
            # been watering
            while plants and plants[0] <= A:
                A -= plants[0]
                plants.pop(0)

            while plants and plants[-1] <= B:
                B -= plants[-1]
                plants.pop(-1)

            # now we refill, if we can do it in 1 go, refill once, and do rest
            # else refill both

            # able water them all with 1 refill
            if not plants:
                break

            if sum(plants) <= max(capacityA, capacityB):
                refill += 1
                break
            else:
                refill += 2
                A = capacityA
                B = capacityB

        return refill
        """