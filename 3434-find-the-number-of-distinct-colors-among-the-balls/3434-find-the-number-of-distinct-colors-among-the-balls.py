class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # l + 1 balls, with labels 0 to l
        # balls uncoloured
        # query, mark x ball with y
        # then return result where i denote num of colours after ith query
        # e.g
        # 0 0 0 0 0
        #   4
        #   4 5
        #   3 5
        #   3 5 4
        # could go through each query, update, then see what colours are like
        # n^2
        # or keep hashmap of each pos = colour
        # hashmap of colour = count
        # set = colours so far
        posMap = {}
        colMap = {}
        cur = set()

        result = []

        for [ball, colour] in queries:
            if ball in posMap:
                # else already exist
                prev = posMap[ball]
                colMap[prev] -= 1

                # no more
                if colMap[prev] == 0:
                    cur.remove(prev)
            posMap[ball] = colour
            #brand new colour so we add to current
            if colour not in colMap or colMap[colour] == 0:
                cur.add(colour)
            colMap[colour] = colMap.get(colour,0) + 1

            result.append(len(cur))
        return result



            