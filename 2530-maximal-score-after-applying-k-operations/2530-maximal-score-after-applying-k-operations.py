class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # score = 0
        # choose an index in nums and increase score by nums[i]
        # then replcae said nums i with ceil nums[i] / 3
        # return max score after k operations
        # be greedy -> get biggest one and add that, then update value
        # put into heap again, sorts itself, and returns back
        result = 0
        nums = [-x for x in nums]

        heapq.heapify(nums)

        while k > 0:
            value = heapq.heappop(nums)
            result += (-1 * value)
            value = (ceil((value / 3) * -1)) * -1
            heapq.heappush(nums,value)
            k -= 1
        return int(result)