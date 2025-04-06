class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # dp i power using spell up to i
        # then we store so when we do power up to i + whatever, we can combine power computed before

        # find count of each pwr
        count = Counter(power)

        # find strength aka pwr * amount
        strength = {k: k * count[k] for k in count}

        spells = [0,0,0] + sorted(list(strength.keys()))

        n = len(spells)
        dp = [0] * n

        for i in range(3, n):
            if spells[i] - spells[i-1] > 2:
                dp[i] = dp[i-1] + strength[spells[i]]
            elif spells[i] - spells[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + strength[spells[i]])
            else:
                dp[i] = max(dp[i-1], dp[i-3] + strength[spells[i]])

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
