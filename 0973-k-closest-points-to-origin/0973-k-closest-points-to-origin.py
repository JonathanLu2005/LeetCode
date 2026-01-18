class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # find point that closest to 0,0
        # we can calculate the distance from the toher points to the origin
        # sort those, and return the kth closest
        # minheap, return all k closest, coordinates
        minheap = []
        for [x,y] in points:
            distance = math.sqrt((x-0)**2 + (y-0)**2)
            minheap.append((distance, (x,y)))

        heapq.heapify(minheap)

        result = []

        while k > 0:
            value, key = heapq.heappop(minheap)
            x, y = key
            result.append([x,y])
            k -= 1
        return result