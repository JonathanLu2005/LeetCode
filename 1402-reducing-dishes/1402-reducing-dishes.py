class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # return max like time coefficient
        # we do time i * satisfaction i
        # prepare dishes in any order, and discard dishes
        # so greedy is to get all the positives, from smallest to biggest
        # however, it might be worthwhile to keep some of the negatives
        # as the negative + bigger * 1 more > bigger without negative to increase multiplication
        # fyi time start from 1 to n
        # we could sort it, calculate what its like
        # and then we can slowly remove a dish at a time or whatever and see if it gets better till we reach a positive
        # as no more point to keept trying

        # -9 -8 -1 0 5 = -28 + 25 = -3
        # -8 -1 0 5 = -10 + 20 = 10
        # -1 0 5 = 14
        # 0 5 = 10
        satisfaction = sorted(satisfaction)
        result = 0
        n = len(satisfaction)

        for i in range(0,n):
            count = 1
            current = 0
            
            for j in range(i,n):
                value = satisfaction[j]
                current += (value * count)
                count += 1
            
            result = max(result,current)

            if satisfaction[i] >= 0:
                break
        return result