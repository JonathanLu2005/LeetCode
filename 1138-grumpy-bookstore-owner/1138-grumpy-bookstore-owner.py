class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # n minutes
        # n cutsomer enter at ith minute
        # 1= grumpy, 0 = not grumpy
        # when owner grumpy, customer are unsatisfied
        # else satisfied
        # can be not grumpy for consecutive minutes used once
        # return max number customer satisifed
        # i = number of customer enter
        # count happy customer by default
        # then find window where most customers will be happy when guy is grumpy
        if minutes == len(customers):
            return sum(customers)
        
        window = 0
        alreadyHappy = 0

        for i in range(0, minutes):
            if grumpy[i] == 1:
                window += customers[i]
            else:
                alreadyHappy += customers[i]

        maxResult = window

        for i in range(minutes, len(customers)):
            if grumpy[i-minutes] == 1:
                window -= customers[i-minutes]

            if grumpy[i] == 1:
                window += customers[i]
                maxResult = max(maxResult, window)
            else:
                alreadyHappy += customers[i]

        return alreadyHappy + maxResult

            