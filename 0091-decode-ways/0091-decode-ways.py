class Solution:
    def numDecodings(self, s: str) -> int:
        # decision is only double digits if its 1 or 2
        # otherwise need to skip and save time!
        # and if take 1 need to be 0-9, 2 need to be 0-6
        # thats how u decide to take double digits! else just choose the 1
        # and if next val is 0 gotta take it
        # would be dp[i] = dp[i+1] + dp[i]
        # as those r only 2 decisions
        # rmbr can add it like that

        # with cache, 1's there as base case if empty
        dp = { len(s) : 1 }

        def dfs(i):
            # been cached or end of string
            if i in dp:
                return dp[i]
                # cant do anything else as cant parsed simply 0 and stuff like 01
            if s[i] == "0":
                # invalid
                return 0
            
            res = dfs(i+1)
            # otherwise take next step

            # if have a 2nd char that goes after this one
            # no need for and for 1 as can be anytihng between 0-9 but other need be 0-6
            # know to take 2 steps as could possibly be possible
            if (i + 1 < len(s) and (s[i] == "1" or 
            s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
                # so know result

            # 
            dp[i] = res

            return res
        print(dp)

        return dfs(0)

        """
        arr = [str(x) for x in range(1,27)]
        res = [0]
        steps = []
        


        def backtrack(index):
            if index + 1 >= len(s):
                if index + 1 == len(s):
                    res[0] += 1
                return

            
            if (index + 1) in steps:
                pass
            elif s[index + 1] in arr:
                backtrack(index + 1)
            else:
                steps.append((index + 1))
            
            if (index + 1, index + 3) in steps:
                pass
            elif s[index + 1: index + 3] in arr:
                backtrack(index + 2)
            else:
                steps.append((index + 1, index + 3))

        backtrack(-1)
        return res[0]"""


        