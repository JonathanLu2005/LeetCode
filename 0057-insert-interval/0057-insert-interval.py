class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 4 cases,1 we might have to add it at start,or at end, or merge into interval or inbetween
        # if the interval end is < first interval start, go at start
        # if interval start is > last interval end, go at end
        # go htrough each interval
        # if our inserted interval, start and end, conflict with the current interval start and end
        # we merge together and remove that interrval, and keep going, until no more merges
        # if it collides, we merge them, else if next guy above doesnt, then we just add it in there
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        x, y = newInterval

        if y < intervals[0][0]:
            intervals.insert(0,newInterval)
            return intervals
        if x > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        n = len(intervals)
        i = 0
        added = False

        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]

            if x <= end and y >= start:
                x = min(start,x)
                y = max(end,y)
                intervals.pop(i)
                n -= 1
            elif x < start and y < start:
                intervals.insert(i,[x,y])
                added = True
                break
            else:
                i += 1

        if not added:
            intervals.append([x,y])

        return intervals
