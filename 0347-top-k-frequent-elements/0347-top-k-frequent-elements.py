class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use hashmap to store everything, then heap to order it, and keep popping heap k times till we get it
        
        minheap = []

        hashmap = {}

        for x in nums:
            hashmap[x] = hashmap.get(x,0) - 1
        
        for key, value in hashmap.items():
            heapq.heappush(minheap, (value, key))
        
        heapq.heapify(minheap)

        result = []

        while k > 0 and len(minheap) > 0:
            value, key = heapq.heappop(minheap)
            result.append(key)
            k -= 1
        return result
        