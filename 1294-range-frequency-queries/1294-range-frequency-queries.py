class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.hashmap = {}

        n = len(arr)

        for i in range(0,n):
            val = arr[i]

            if val not in self.hashmap:
                self.hashmap[val] = []
            self.hashmap[val].append(i)
        

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.hashmap:
            return 0

        indexes = self.hashmap[value]
        l = bisect.bisect_left(indexes,left)
        r = bisect.bisect_right(indexes,right)
        return r - l
                

        # binary search for left, then right
        # then use values to determine index

        # if r == l, its either 1 or 0

    # let say we want indexes between 2 4, and our indexes are 1 3 5
    # so we want left 2, returns position of 1, but incorrect so + 1
    # want 4, cant find it, so retunr index of 5, so return m - 1
    # so if both r == l, return 1
    # but if not, return r - l + 1


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

# idea is that given 2 values, aka a subarray so elements from index left to right
# find number of whatever appears in there
# go through each value, and store every index
# such that when we access that value, we check how many numbers are within range
# and by that we're able to find number of elements