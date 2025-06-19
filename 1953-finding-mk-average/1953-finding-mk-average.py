class MKAverage:

    def __init__(self, m: int, k: int):
        self.array = []
        self.m = m
        self.k = k
        self.size = 0
        self.now = False
        self.half = []
        self.sorted = []

    def addElement(self, num: int) -> None:
        if not self.now:
            self.array.append(num)
            self.size += 1
        else:
            self.sorted.remove(self.half[0])
            self.half.pop(0)

            self.half.append(num)
            self.sorted.add(num)

    def calculateMKAverage(self) -> int:
        if not self.now:
            if self.size < self.m:
                return -1
            else:
                self.now = True
                self.half = self.array[self.size-self.m:]
                self.sorted = SortedList(self.half)
        answer = self.sorted[self.k:self.m-self.k]
        return int(sum(answer) / (self.m - (2*self.k)))
        
# if stream is < m, mk average is - 1
# else, copy last m elements
# remove smallest k elements and largest k elements
# calculate average value rounded down

# if n < m, just continue
# once we hit > m
# have a new data structure to hold last m
# so we just add to that and remove index 0
# and once we wanna do thingy, sort it, and return whatevers within
# could just have a sorted list version and use other array to track what to remove next
# and able return value

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()