class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # get count of each value with maxheap
        # get most popular then whatever next popular
        # so forth s.t. keeps a train of different values going
        hashmap = {}

        for x in barcodes:
            hashmap[x] = hashmap.get(x,0) + 1

        result = []

        maxHeap = [(-value, key) for key, value in hashmap.items()]
        heapq.heapify(maxHeap)

        prev = heapq.heappop(maxHeap)
        current = []
        

        while maxHeap:
            # add key, 
            newValue = prev[0] + 1
            key = prev[1]
            result.append(key)

            current = heapq.heappop(maxHeap)
            if newValue != 0:
                heapq.heappush(maxHeap, (newValue, key))
            prev = current

        result.append(prev[1])

        return result
