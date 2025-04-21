class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # infinite 2d grid, aim for target, ghosts exists
        # either move l r u d or stay still (happens simultaneously)
        # escape iff reach target before ghost reaches you
        # return true if possbiel escape, else false

        # start at 0,0
        # i think the key tactic here is to determine how many moves the ghosts need to take to get to target
        # versus you
        # because if they can get to target before you, possibly means they can intersect you regardless

        fastestGhost = float("inf")

        targetX = target[0]
        targetY = target[1]

        player = abs(targetX) + abs(targetY)

        for [x,y] in ghosts:
            moves = abs(x-targetX) + abs(y-targetY)
            fastestGhost = min(fastestGhost, moves)

        return (player < fastestGhost)
