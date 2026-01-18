class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # so find the kth largest number
        # could just shove it in a heap and keep popping till get k

        minheap = [-1 * x for x in nums]
        heapq.heapify(minheap)

        while k > 0:
            result = -1 * heapq.heappop(minheap)
            k -= 1
        return result