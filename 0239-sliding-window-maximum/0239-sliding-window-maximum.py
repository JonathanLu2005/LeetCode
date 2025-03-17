class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # idea is deleting elements that wont be max within window
        # use a deque, always decreasing
        # moment a value is greater than rest of deque
        # will pop rest
        # will add leftmost value to output
        # then shift window
        # basically to avoid redoing work, will just delete everything
        # and keep max
        # this is a monotic decreasing queue
        # use queue to add and remove elements in o(1)
        # only remove smaller elemnts if exist
        # keep it in decreasing order
        # pop when its no longer within bounds
        # pop right most to keep it in decreasing monotonic

        # r pointer to keep adding values
        # but key is having a monotonic decreasing queue to hold max
        # then if we meet widnow size, and q 0 index is smalelr than l
        # means we've an element outside of bound so remove

        output = []
        l = r = 0

        q = collections.deque()

        while r < len(nums):
            # remove to keep decreasing monotonic
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left if met window size
            # hence why we store indexes
            if l > q[0]:
                q.popleft()
            
            # if in window size, add max val
            # increment l when we reach k
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

        
        """
        
        # have nums and window k
        # then we get max of each widnow and return it

        # we just need to check the last / next element tbf and see if thats greater
        # only issue is when we reach outside of k and need to replace it
        # then we need to find next biggest

        # could pop k times get biggest
        # then pop next see whose bigger
        # then so on
        window = nums[0:k]
        results = []

        results.append(max(window))

        for i in range(k, len(nums)):
            window.pop(0)
            window.append(nums[i])
            results.append(max(window))

        return results
        """