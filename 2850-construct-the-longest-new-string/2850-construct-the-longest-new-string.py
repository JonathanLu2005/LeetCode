class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # cant have AAA, BBB
        # want get max length of new string

        # and we've AA, BB, AB
        # try exhaust them all, so let say we've 5, 10, of AA and BB
        # obviously we do AABB AABB AABB AABB AABB AABB (now we only have 5 BB)
        # but we can just throw random AB
        # AB AB AB then we do AA and at end BB AB AB can only do AA
        # so rule for us to use AB is
        # if use AB at start, tehn AA starts
        # if we use AB at end, then BB must end
        # and if we've many BB we can do BB AB AB AB AA BB AA BB AB AB AA
        # ah so we can only do x amount of AA BB
        # then we can fit 1 more BB or AA in (far left and far right)
        # and rest are just AB AB!
        

        #number = min(x,y) * 2
        #x -= number // 2
        #y -= number // 2
        # this forms our basis of AA BB AA BB
        # then we simply apply all Z amoun of AB
        #number += z

        # then we can only fit in 1 more of x or y
        #if x != 0 or y != 0:
        #    number += 1

        #return number * 2

        # refactoring code to be nice
        number = min(x,y) * 2
        if (x+y) > number:
            number += 1
        number += z
        return number * 2