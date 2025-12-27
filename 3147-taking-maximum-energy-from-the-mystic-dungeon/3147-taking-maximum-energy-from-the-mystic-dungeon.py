class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # n magicians
        # each give energy
        # some take energy
        # after getting energy from i, get transported to i+k
        # keep going till i+k dont exist
        # have a start, and then keep teleport, absorbing energy
        # return max energy cold gain
        # i mean theres a pattern because it'll keep like frog jumps
        # OH WAIT I HAVE AN IDEA
        # because we can only have so many intervals
        # e.g for k = 3 would be like
        # 0 1 2
        # we can put them in bins
        # circular rotation of adding numbers, like revolver chamber
        array = [0] * k

        for i in range(0,len(energy)):
            key = i % k
            value = energy[i]

            array[key] = max(array[key] + value, value)
        return max(array)