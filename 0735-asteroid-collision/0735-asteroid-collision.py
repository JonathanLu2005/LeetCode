class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # val = size
        # sign = direction
        # move same speed
        # if 2 meet, smaller explode, if both same both explode
        # moving in same direction never meet
        # need to find all the negative values
        # then move backwards
        # could just loop backward
        # and if we find negative itll eventually collide, just determine if both explode, just it or other and continue

        i = len(asteroids) - 1

        while i > 0:
            c = asteroids[i]
            nc = asteroids[i-1]

            # c move back, nc move forward
            if c < 0 and nc > 0:
                c = abs(c)
                
                # explode both
                if c == nc:
                    asteroids.pop(i)
                    asteroids.pop(i-1)
                    i -= 1
                # explode nc
                elif c > nc:
                    asteroids.pop(i-1)
                    #i -= 1
                # explode c
                elif nc > c:
                    asteroids.pop(i)
                    #i -= 1

                if i >= len(asteroids):
                    i -= 1
            else:
                i -= 1

        return asteroids