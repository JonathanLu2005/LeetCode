class SeatManager:

    def __init__(self, n: int):
        seats = [x for x in range(1,n+1)]
        heapq.heapify(seats)
        self.seats = seats

    def reserve(self) -> int:
        seat = heapq.heappop(self.seats)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats,seatNumber)
        
# have seats 1 to n 
# manage n seats from 1 to n
# we fetch smallest unreserved seat, reserve it and return value
# orwe can unserve it
# the key is that we reserve the SMALLEST seat
# i think to achieve that is by having a heap
# with a minheap we can keep track of smalelst seat
# and reserve that if possible
# otherwise we can just add it back in

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)