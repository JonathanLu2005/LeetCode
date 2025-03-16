class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # linear is
        # get all positives
        # then for i through it
        # and if index i isnt 1 e.g 0 should be 1
        # then return that
        
        positiveNums = [x for x in nums if x > 0]

        if positiveNums == []:
            return 1

        positiveNums = sorted(list(set(positiveNums)))

        for i in range(0, len(positiveNums)):
            if positiveNums[i] != (i+1):
                return (i+1)

        return max(positiveNums) + 1