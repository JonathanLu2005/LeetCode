class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter = {}

        for x in nums2:
            self.counter[x] = self.counter.get(x,0) + 1

    def add(self, index: int, val: int) -> None:
        key = self.nums2[index]
        self.counter[key] -= 1
        self.nums2[index] += val
        key = self.nums2[index]
        self.counter[key] = self.counter.get(key,0) + 1


    def count(self, tot: int) -> int:
        res = 0
        for x in self.nums1:
            key = tot - x
            res += self.counter.get(key,0)
        return res

# could prestore ALL pairs
# so pair = this value
# and then for each value = store all pairs
# HOWEVER, everytime we add value, we find the pair, we get its value
# change its value, change count of value whatever
# then when we return we just return

# nah, instead hold nums1, make nums2 as a hashmap
# everytme we change index, we change count in hashmap
# then for count, we go through all values in nums1, tot - nums1, see if exist
# return

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)