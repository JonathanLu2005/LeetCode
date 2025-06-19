class MedianFinder:

    def __init__(self):
        self.array = SortedList([])

    def addNum(self, num: int) -> None:
        self.array.add(num)

    def findMedian(self) -> float:
        n = len(self.array)

        if n % 2 == 1:
            target = int(n // 2)
            return self.array[target]
        else:
            target = int((n/2) - 1)
            median = self.array[target] + self.array[target+1]
            return median / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()