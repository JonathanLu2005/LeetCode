class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # iterate, for each key value pair, increment tthe key appearance
        # then moment we hit >= 2, we store that into set
        # return set as list
        hashmap = {}
        result = set()

        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1
            if hashmap[x] >= 2:
                result.add(x)

        return list(result)