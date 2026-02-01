class Solution:
    def findScore(self, nums: List[int]) -> int:
        # score=0
        # choose smallest int not marked
        # if tie, chosoe one with smallest index
        # add value to score
        # mark element and its 2 adjacent
        # repeat until all are marked
        # we could use heap and an array to mark dead states
        # algorithm -> find smallest value if not marked, if its tie choose one with smallest index
        # and then marked the ones next to it
        # return result
        # heap -> we can order it by (value,index)
        # get smallest value and smallest index
        # easily get theabove
        # to do the marking
        # wehave aset, we addthe index in the set, then we also add index + 1, index - 1
        # s.t. when we getthe next value in heap, if its index is in marked, then we dont bother
        # because its been marked
        result = 0
        n = len(nums)
        heap = []

        for i in range(n):
            value = nums[i]
            heap.append((value,i))

        heapq.heapify(heap)
        marked = set()

        while heap:
            value, index = heapq.heappop(heap)

            if index not in marked:
                result += value
                marked.add(index)
                marked.add(index+1)
                marked.add(index-1)
        return result