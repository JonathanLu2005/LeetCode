class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # we could just add it in, sort it, and merge but that'll be nlogn
        # so go through everything see if it overlap if so merge, else add to start or end
        intervals.append(newInterval)
        intervals = sorted(intervals)

        n = len(intervals)
        i = 0

        while i < n-1:
            curX, curY = intervals[i][0], intervals[i][1]
            nexX, nexY = intervals[i+1][0], intervals[i+1][1]

            if nexX <= curY:
                intervals[i] = [min(curX,nexX),max(curY,nexY)]
                intervals.pop(i+1)
                n -= 1
            else:
                i += 1
        return intervals