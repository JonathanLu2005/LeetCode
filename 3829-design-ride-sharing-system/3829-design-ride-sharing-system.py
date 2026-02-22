class RideSharingSystem:

    def __init__(self):
        self.riders = []
        self.drivers = []
        self.cancel = set()
        self.riderCheck = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.riderCheck.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.riders and self.drivers:
            while self.riders and self.riders[0] in self.cancel:
                rider = self.riders.pop(0)
                self.cancel.remove(rider)
                self.riderCheck.remove(rider)

            if self.riders:
                rider = self.riders.pop(0)
                driver = self.drivers.pop(0)
                return [driver,rider]

        return [-1,-1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riderCheck:
            self.cancel.add(riderId)

"""
get ride requests
get driver availability

rider => ride
driver => available

match by order arrived

add rider, add driver

match earliest rider and driver
=> array s.t. first element = earliest, queue, FIFO

cancel ride request, rider ID

rider array => add rider
driver array => driver
match => get first element of either, return their id else -1 -1

lazy deletion => cancel rider => add into a set
match => if the rider is inside the set, then we dont match and discard rider, and check the next guy
"""

# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)