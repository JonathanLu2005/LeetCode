class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # largest, minheap, so make everything negative
        # and return k

        heap = [-x for x in nums]
        heapq.heapify(heap)

        while k > 0:
            result = heapq.heappop(heap)
            k -= 1
        return (result * -1)