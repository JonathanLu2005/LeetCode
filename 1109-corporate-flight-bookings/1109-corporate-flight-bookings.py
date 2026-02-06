class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # lol its jsut classic prefix sum
        # find the longest booking and smallest
        window = [0] * (n+1)

        for [first, last, seats] in bookings:
            window[first-1] += seats
            window[last] -= seats

        result = []
        count = 0

        for x in window:
            count += x
            result.append(count)
        result.pop(-1)
        return result