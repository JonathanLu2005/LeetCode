class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # given an array, store the indexes
        # choose an index to choose from
        # then pass an array of indexes to skip
        # so chose 2, skip 2, now only 0 1 left, choose 0, skip 1

        # revolve our choices by a count hashmap
        res = []
        perm = []
        count = { n:0 for n in nums }
        
        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in count:
                # allow choose num
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()
        
        dfs()
        return res


        """
        
        res = []

        def dfs(indexes, arr):
            if len(arr) == len(nums) and arr not in res:
                res.append(arr.copy())
                return

            for i in range(0, len(nums)):
                if i not in indexes:
                    indexes.append(i)
                    arr.append(nums[i])

                    dfs(indexes, arr)

                    indexes.remove(i)
                    arr.remove(nums[i])


        dfs([],[])

        return res
        """