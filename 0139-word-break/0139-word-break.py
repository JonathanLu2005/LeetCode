class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # go through the string and see if exist in dict
        # follow decision tree, then put into cache and solve

        # descition tree start at i = 0, find word there, then subproblem find word in remainder of string
        # have 2 choice if figured it out, can accept or keep going to see if theres another
        # decision based on the dict
        # check if the word from dict exist in s, not other way round
        # so path is check if word exist in frist part of the string
        # eg leetcode, check if code at start, nop, then check leet yes
        # then for last 4 check leet and code
        # reason we've a cache, let say we had another path, and we're on i = 5, and we already tried the other option
        # then we can access cache to avoid the work!
        # so try all option, store our progress, and use that to optimise the decision tree
        # go backwards and see if the letter matches any of the words or not well
        # able use work to determine if psosible for other
        # eg leetcode, let say 2 is false, then rest is false as wont have the window we want
        # able get the DP index and whantot to get the words we want

        dp = [False] * (len(s) + 1)
        #base case where entire string is true for 1 word
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # see if starting at i, if possible to actually make the word length wise
                if (i+len(w)) <= len(s) and s[i: i + len(w)] == w:
                    # enough char to compare and if length is equal
                    dp[i] = dp[i+len(w)]
                    # able to find 1 way to word breka it, no need to do more
                if dp[i]:
                    # already possible
                    break
        # keep working backward to see if possible then yh
        return dp[0]

        # go backwards and first check if length is enough for word
        # and if word matches
        # if so then whatever i is, is same as dp i + len(w)
        # so's true
        # then keep going backwards and if i's true then shown is possible to braek
        # so just return the first 0 aka where we store the overallr esult
                




        """
        # see if the word given can be broken up to be part of the dictionary
        # can just for loop through word till it fits
        # keep going and change the word we're holding rn 
        # see if entire thing works 
        # if not return false or smth

        word = "" 
        for i in range(0, len(s)):
            word += s[i]

            print(word)
            if word in wordDict:
                word = ""

        if word == "":
            return True
        return False
        """