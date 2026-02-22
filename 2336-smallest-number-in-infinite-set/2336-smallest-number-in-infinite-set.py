class SmallestInfiniteSet:

    def __init__(self):
        self.numbers = set()
        self.current = 1

    def popSmallest(self) -> int:
        if self.numbers:
            result = min(self.numbers)
            self.numbers.remove(result)
            return result
        self.current += 1
        return self.current - 1

    def addBack(self, num: int) -> None:
        if num < self.current:
            self.numbers.add(num)
        
"""
set => from 1 to infinity
so return smallest should be like 1 => 2 => 3 => 4 => 5
however we can add back

maintain current smallest number
if add back > smallest number, we dont care about it
if add back < smallest number

array = just for add back
so next time we ask to pop, we need to first
clear out the array as they've smallest number
once array is gone, we can continue back on current smallest value and onwards

1 => 2 => 3 => 4 => 5
[1,2,3]

1 2 3, empty, 5 6 7

could have array, and check for min

nlogn

n => ensure it stay sorted
just add => min which is n
"""

"""
return 1, current 2
hold 1

"""

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)