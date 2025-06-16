class Solution:
    def reorganizeString(self, s: str) -> str:
        # get hashmap of each letter
        # and try alternating every one with haep to choose max value
        # and if run out of characeters such that have to have same adjacent one, return ""
        hashmap = {}

        for x in s:
            hashmap[x] = hashmap.get(x,0) + 1

        result = ""

        maxHeap = [(-value,key) for key, value in hashmap.items()]
        heapq.heapify(maxHeap)

        value, key = heapq.heappop(maxHeap)

        while maxHeap:
            result += key
            nextValue, nextKey = heapq.heappop(maxHeap)

            if -value > 1:
                heapq.heappush(maxHeap, (value + 1, key))
            value = nextValue
            key = nextKey

        if -value == 1:
            result += key
            return result
        return ""