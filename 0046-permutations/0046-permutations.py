class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]

        # right logic, wrong exeuction 
        # so he popped it off (i wanna do)
        # then recursive do it agian but smaller nums (what i did)
        # then we get result and put into perm
        # then put into result
        # and put it back to nums
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)

        return res


        """
        res = []
        
        def backtrack(nums,subset):
            if nums == None:
                res.append(subset.copy())
                return 

            for x in nums:
                subset.append(x)
                print(nums)
                backtrack(nums.remove(x), subset)
                print(nums)
                nums.append(x)
                print(nums)
                subset.pop()
            return

        backtrack(nums,[])
        return res"""