class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])
            right += 1

        return profit

        # sliding window is just 2 pointers with extra steps
        # so kinda like greedy, i.e here if we get a new small value thats our new left
        # as want buy to be small as possible, hence dictate when left moves
        # otherwise move right as usual