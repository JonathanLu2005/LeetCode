class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # dp i power using spell up to i
        # then we store so when we do power up to i + whatever, we can combine power computed before

        # find count of each pwr
        count = Counter(power)

        # find strength aka pwr * amount
        strength = {k: k * count[k] for k in count}

        # all power we can choose from
        spells = [0,0,0] + sorted(list(strength.keys()))

        # craetes dp
        n = len(spells)
        dp = [0] * n

        # essentially our choices are we take current cuz it doesnt affect anything
        # orwe take current + spell 2 ago, or keep spell 1 ago
        # or take current + spell 3 ago, or keep spell 1 ago
        # and we store max as we build along
        # bc we break it into sub problem e.g 10 spells, looke at first x then y then build to 10
        # find most optimal at like 1-8 so when we go to 9, we can easily apply to 6 7 8
        # as only time it gets affected

        # first 3 are padding, rest are spells
        for i in range(3, n):
            # if we can apply this spell aka gap is > 2, apply might asw if we can use it
            # if fail mean i-1 cant use aka within 2
            # like 3 6, 6 doesnt affect 3 so can take
            if spells[i] - spells[i-1] > 2:
                dp[i] = dp[i-1] + strength[spells[i]]
            # current spell is close from previous, we either skip aka continue prev, or take where we discard prev and take dp from before
            # i-1 is prev
            # this ie like 1 3 4, we either take optimal of 3 or do 4 + 1
            elif spells[i] - spells[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + strength[spells[i]])
            # if we've smth like 3 4 5 6, obv we cant use 6 if 5 and 4 r too close and used
            # so we're testing whats better, 5, or 3 + 6
            else:
                dp[i] = max(dp[i-1], dp[i-3] + strength[spells[i]])
        # retun best at end
        return dp[-1]

        """ failed attempt
        # hashmap, store power = amount
        # have set of options
        # keep going with options
        # else add to array or set we cant use options
        hashmap = {}

        for x in power:
            hashmap[x] = hashmap.get(x,0) + 1

        options = sorted(set(power))

        # dp
        cache = {}


        def backtrack(index, result, ban):
            # key is what option we're on and what our ban looks like
            key = (index, frozenset(ban))

            # if already exist dont need to recompute
            # this is backtracking 2^n so we can recompute values
            if key in cache:
                return cache[key]
            if index == len(options):
                return result

            # skip
            skip = backtrack(index + 1, result, ban)

            # dont skip
            value = options[index]
            take = result
            if value not in ban:
                take += ((value) * (hashmap[value]))

                newBan = set(ban)
                newBan.update([value, value - 1, value - 2, value + 1, value + 2])

                take = backtrack(index + 1, take, newBan)

            # take value from skip and take, and store max
            # so next time we approach this again with different combo of take and skip
            # can reuse
            cache[key] = max(skip, take)
            return cache[key]

        return backtrack(0,0,set())
        """
