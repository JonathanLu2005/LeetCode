class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        hashmap = {}
        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1

        for num in sorted(hashmap.keys()):
            while hashmap[num] > 0:
                for x in range(k):
                    key = num + x

                    if hashmap.get(key,0) <= 0:
                        return False
                    hashmap[key] -= 1

        return True