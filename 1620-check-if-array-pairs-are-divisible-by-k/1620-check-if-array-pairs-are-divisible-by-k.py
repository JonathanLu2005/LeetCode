class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # mod, get the remainder
        # bc let say we've 1 and 4 and k = 5, all we acre about is getting a number with that remainder
        # we store all the remainder and how many numbers are in there
        # then as we go through each remainder, we can check if we've enough numbers??

        hashmap = {}

        for x in arr:
            remainder = x % k
            hashmap[remainder] = hashmap.get(remainder,0) + 1

        for remainder in range(1, math.ceil(k/2)):
            pair = hashmap.get(k-remainder,0)
            current = hashmap.get(remainder,0)

            if pair != current:
                return False
        zero = hashmap.get(0,0)
        return (zero % 2 == 0)