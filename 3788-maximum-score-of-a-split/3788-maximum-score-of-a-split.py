class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        # n numbers
        # choose any index
        # and we'll get the sum of all numbers to left of split
        # and min val of right of split
        # and then do left - irght = score
        # i mean one way to do this is try every value haha!
        # can do 10 - - 5 = 15
        # go on 10 -1 - - 5
        # whatever
        # just wondering if getting the min will be crazy computation :p
        # it'll be n^2...
        # we could just sort it 
        # and as we keep going 
        # and if we know the current index aint the min we keep going else we swap
        hashmap = {}

        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1
        track = nums.copy()
        track = sorted(track)
        minValue = track[0]

        result = float("inf") * -1
        current = 0

        nums.pop(-1)

        for x in nums:
            current += x

            hashmap[x] -= 1

            if x == minValue:
                while hashmap[minValue] == 0:
                    track.pop(0)
                    minValue = track[0]

            if (current - minValue) > result:
                result = current - minValue

        return result