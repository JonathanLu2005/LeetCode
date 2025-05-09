class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # for each value, keep count of what indices they appear in
        # and when we combine those if length equal to length needed
        # possible
        # then we just take away whatever they intersect from length of either
        # and use that as min

        top = {}
        bottom = {}
        n = len(tops)
        values = set()

        for i in range(0,n):
            t = tops[i]
            b = bottoms[i]

            if t not in top:
                top[t] = set()
            top[t].add(i)

            if b not in bottom:
                bottom[b] = set()
            bottom[b].add(i)

            values.add(t)
            values.add(b)

        res = float("inf")

        for v in values:
            t = top.get(v,set())
            b = bottom.get(v,set())

            total = t.union(b)
            # possible
            if len(total) == n:
                i = len(t.intersection(b))

                r = min(len(t) - i, len(b) - i)
                res = min(res,r)

        if res == float("inf"):
            return -1
        return res
            
            

