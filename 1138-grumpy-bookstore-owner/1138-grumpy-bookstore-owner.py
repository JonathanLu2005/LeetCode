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
        
        window = []
        alreadyHappy = 0

        for i in range(0, minutes):
            if grumpy[i] == 1:
                window.append(customers[i])
            else:
                window.append(0)
                alreadyHappy += customers[i]

        maxResult = sum(window)

        for i in range(minutes, len(customers)):
            window.pop(0)

            if grumpy[i] == 1:
                window.append(customers[i])
                maxResult = max(maxResult, sum(window))
            else:
                window.append(0)
                alreadyHappy += customers[i]

        return alreadyHappy + maxResult

            