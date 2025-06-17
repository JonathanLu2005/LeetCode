class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # for each node, map it to its enghibours, and get k max ones
        if edges == []:
            return max(vals)
        hashmap = {}
        keys = set()

        for [x,y] in edges:
            if x not in hashmap:
                hashmap[x] = []
                keys.add(x)
            if y not in hashmap:
                hashmap[y] = []
                keys.add(y)

            hashmap[x].append(vals[y])
            hashmap[y].append(vals[x])

        result = -1 * float("inf")

        for key in keys:
            values = hashmap[key]
            values = sorted(values)[::-1]

            i = 0
            temp = 0
            while i < min(k,len(values)):
                v = values[i]
                if v > 0:
                    temp += v
                else:
                    break
                i += 1
            #print(key)
            temp += vals[key]
            result = max(result,temp)
        return max(result,max(vals))
            
