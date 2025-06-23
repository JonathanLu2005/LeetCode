class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.array = encoding

    def next(self, n: int) -> int:
        while n > 0:
            if not self.array:
                return -1

            value = self.array[0]
            key = self.array[1]

            if value >= n:
                self.array[0] -= n

                if self.array[0] == 0:
                    self.array.pop(0)
                    self.array.pop(0)
                return key
            elif value < n:
                n -= value
                self.array.pop(0)
                self.array.pop(0)





# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)