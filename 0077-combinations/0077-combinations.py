class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            # base case then return back, 
            if len(comb) == k:
                res.append(comb.copy())
                return 

            # as we return, comb.pop() gest to our OG pos
            # call backtrack with i+1 so we can try get next num
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()

        # calling backtrack
        backtrack(1, [])
        return res

        """
        res = []
        subset = []

        def dfs(i, subset):
            if len(subset) == k:
                res.append(subset.copy())
                return res 

            for x in range(i+1, n+1):
                subset.append(x)
                dfs(x, subset)
                subset.pop()

        dfs(0, [])
        return res"""
