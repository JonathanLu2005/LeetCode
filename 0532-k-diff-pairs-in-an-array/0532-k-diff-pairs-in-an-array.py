class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # count pairs where i != j
        # nums i - nums j = k
        # ok so pairs where their num differnce is k
        # only care about unique pairs
        # for each value can do 3 - k and 3 + k and check if in there
        # if so increment res and put value somewhere so we can check if it exists already 
        res = 0

        hashmap = {}

        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1

        nums = set(nums)

        visited = set()

        for x in nums:
            hashmap[x] -= 1
            t1 = hashmap.get(x+k,0)
            t2 = hashmap.get(x-k,0)

            v1 = frozenset({x+k, x})
            v2 = frozenset({x-k, x})

            if t1 > 0 and v1 not in visited:
                res += 1
                visited.add(v1)
            if t2 > 0 and v2 not in visited and x+k != x-k:
                res += 1
                visited.add(v2)

            hashmap[x] += 1

        return res