class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # mass = planet mass
        # asteorids = mass of ith asteroid
        # planet collide with asteorids in any order
        # if planet mass is >= asteoired, asteoired desteoyred
        # planet gain mass of asteoired
        # else planet is cooked
        # retruen true if all asteorids can be destroyed
        asteroids = sorted(asteroids)

        for x in asteroids:
            if mass < x:
                return False
            mass += x
        return True