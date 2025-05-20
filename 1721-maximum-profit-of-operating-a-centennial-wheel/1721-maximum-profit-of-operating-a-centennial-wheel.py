class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        # has for 4 ppl
        # rotate = running cost
        # customers = num customers at ith rotation
        # rotate wheel i times before next customer arrive
        # need board cant make them wait
        # customer pay boarding cost
        # can stop any time then letting them down is free
        profit = 0
        result = 0
        answer = -1

        waiting = 0
        boarded = 0
        turn = 0
        i = 1
        s = sum(customers)
        l = len(customers)

        while boarded != s:
            if turn < l:
                waiting += customers[turn]
                turn += 1

            if waiting >= 4:
                waiting -= 4
                boarded += 4
                profit = (boarded*boardingCost) - (i*runningCost)
            else:
                boarded += waiting
                profit = (boarded*boardingCost) - (i*runningCost)
                waiting = 0

            if profit > result:
                result = profit
                answer = i

            i += 1

        return answer
            
