class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # make it non decreasing by modifiying 1 element
        # so it must be increasing
        # we need to count if the value decrease more than once
        # if so then its beyond recoverable
        # oh shit everything MUST be increasing or we're cooked
        # ok we can do stack
        # so we keep appending
        # if its increasing we're good
        # if it decreased, we get rid of that, thats our last straw
        # amnd if next one is decreasing, we'recooked
        # either we get rid of the small guy, or we get rid of the large guy
        # so if next one isnt bigegr
        # we either pop or not add and we'll continue
        # and if count hit then gg
        if not nums:
            return True

        value = nums.pop(0)
        stackKeep = [value]
        stackSkip = [value]

        countKeep = 0
        countSkip = 0

        for x in nums:
            # skip adding x
            if x < stackSkip[-1]:
                countSkip += 1
            else:
                stackSkip.append(x)

            if x < stackKeep[-1]:
                countKeep += 1
                stackKeep.pop(-1)

                if stackKeep and x < stackKeep[-1]:
                    countKeep += 1
                else:
                    stackKeep.append(x)
            else:
                stackKeep.append(x)

            if (countKeep >= 2) and (countSkip >= 2):
                return False
        return (countKeep <= 1) or (countSkip <= 1)

