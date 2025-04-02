class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # first example 1 5 5 11
        # realise we can get it cool, target is 11
        # so we make array of 11 like
        # [F,F,F, F,F,F, F,F,F, F,F]
        # go from 11 to 1
        # go through each num in nums
        # 1, to make target 11 true, we need  10 to be true is it?
        # false so we continue, we make 1 true so
        # T F F   F F F   F F F     F F
        # go through 5.. with 6 we can make true cuz 6 -5 = 1 is true
        # and continue on
        # until we reach target 11 is true
        # if true means the other half gotta make the target too cuz its split in half
        # adequte nums to achieve target

        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        array = [False] * (target + 1)
        array[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                # find if complement num exist
                if array[i-num]:
                    array[i]= True
        #print(array)
        return array[-1]
