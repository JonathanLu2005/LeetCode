class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        intervals = sorted(intervals)
        while i < n-1:
            curX, curY = intervals[i][0], intervals[i][1]
            nextX, nextY = intervals[i+1][0], intervals[i+1][1]

            if nextX <= curY:
                intervals.pop(i+1)
                intervals[i] = [min(curX,nextX), max(curY,nextY)]
                n -= 1
            else:
                i += 1

        return intervals