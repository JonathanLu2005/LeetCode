class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # add all into heap then try our luck
        heap = []

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                heap.append(matrix[x][y])

        heapq.heapify(heap)

        result = -1
        while k > 0:
            result = heapq.heappop(heap)
            k -= 1

        return result