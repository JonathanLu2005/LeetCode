class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # mass = planet mass
        # asteorids = mass of ith asteroid
        # planet collide with asteorids in any order
        # if planet mass is >= asteoired, asteoired desteoyred
        # planet gain mass of asteoired
        # else planet is cooked
        # retruen true if all asteorids can be destroyed
        
        # 10, 3 4 9 19 21
        # 13 - 17 - 26 - 26 + 19 > 21 ...
        # 5, 4 4 9 23
        # 21 
        asteroids = sorted(asteroids)

        for x in asteroids:
            if mass < x:
                return False
            mass += x
        return True