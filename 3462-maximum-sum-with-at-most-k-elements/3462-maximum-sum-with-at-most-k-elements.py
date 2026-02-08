class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # given grid
        # limits = n
        # k
        # max sum of most k elements fromgrid
        # number of elements from ith row doesnt exceed limit
        # ok...
        # so lets de construct this problem
        # our first objective is to get the max sum via k elements
        # so => this means we want the k biggest elements
        # our second objective is that we dont want to exceed limit of the row
        # so => every time we get the biggest element, we need track which row its from and if we hit the limit
        # to achieve this, for every element we store their value and their row
        # and we put it in a heap such that its ordered so every timewe get element, its the biggest
        # and with a hashmap we increment the count of the row that we took element from
        # and if we hit the limit, we dont include the value, otherwise we keep going
        # nm => get all the elements
        # then its o(n)
        n = len(grid)
        m = len(grid[0])
        heap = []
        
        for i in range(0,n):
            for j in range(0,m):
                value = grid[i][j]
                heap.append((value * -1, i))
        
        heapq.heapify(heap)

        result = 0
        total = sum(limits)
        # what if all the limits are no longer good
        while k > 0 and total > 0:
            value, row = heapq.heappop(heap)

            if limits[row] > 0:
                result += (value * -1)
                limits[row] -= 1
                total -= 1
                k -= 1
        return result

