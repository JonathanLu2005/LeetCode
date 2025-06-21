class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # smooth descent if price keeps coming down by 1
        # icl its a widnow question, find window that does this until doesnt
        # then within that window we automatically can calcualte it
        # bc its finding subarrays
        # can do n * n+1 / 2
        n = len(prices)
        result = 0

        # dont need a window can do this via variables
        length = 1
        prev = prices[0]

        for i in range(1,n):
            next = prices[i]

            if prev - next == 1:
                length += 1
            else:
                result += (length * (length+1)) / 2
                length = 1
            prev = next
        
        result += (length*(length+1)) / 2

        return int(result)

