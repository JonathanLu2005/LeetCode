class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        # nums = initial pos of marble
        # movefrom and moveto = move marbles from movefrom to moveto
        # return sorted list of occupied positions

        # marbles are on posiiton 1 6 7 8 (nums)
        # move position1  to 2, 7 to 9, 2 to 5

        hashmap = {}

        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1

        n = len(moveFrom)

        for i in range(0, n):
            cur = moveFrom[i]
            change = moveTo[i]

            value = hashmap[cur]
            hashmap[cur] -= value
            hashmap[change] = hashmap.get(change,0) + value
        
        result = []

        for key, value in hashmap.items():
            if value > 0:
                result.append(key)

        return sorted(result)