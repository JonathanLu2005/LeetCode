class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # partition so much that in that singular block, only those letters exist in there
        # maths? for each letter, find first index and last index where they appear in
        # ababcbacadefegdehijhklij
        # e.g a = 1 to 9, b = 2 to 6, c = 5 to 8
        # so forth, then try to find intervals that fit in those
        # so merging
        hashmap = {}
        n = len(s)

        for i in range(0,n):
            letter = s[i]

            if letter not in hashmap:
                hashmap[letter] = [i,i]
            else:
                hashmap[letter][1] = i

        intervals = []

        for key, value in hashmap.items():
            intervals.append(value)

        n = len(intervals)
        i = 1

        while i < n:
            curX, curY = intervals[i][0], intervals[i][1]
            prevX, prevY = intervals[i-1][0], intervals[i-1][1]

            # inside, need to merge
            if curX <= prevY:
                newX = min(curX, prevX)
                newY = max(curY, prevY)
                interval = [newX, newY]

                intervals.pop(i)
                intervals[i-1] = interval
                n -= 1
            else:
                i += 1

        result = []

        for [x,y] in intervals:
            result.append(y-x+1)

        return result

        