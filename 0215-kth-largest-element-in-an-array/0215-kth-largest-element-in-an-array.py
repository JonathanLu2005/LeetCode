class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # with heap need to make value negative as doing it by frewquency want to do by how important the number is
        hashmap = {}

        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1

        heap = []

        for key, value in hashmap.items():
            heap.append((-1 * key))

        heapq.heapify(heap)

        while k > 0:
            key = heapq.heappop(heap)
            key *= -1
            result = key
            k -= hashmap[key]

        return result