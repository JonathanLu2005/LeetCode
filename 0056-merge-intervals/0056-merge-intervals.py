class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort it, and if overlap, merge togeter
        # a <= d and c <= b, way to overlap
        # then if overlap, we create them into 1 interval
        # and keep checking next guy if match, else swap to next guy to use as matcher
        intervals = sorted(intervals)
        k = len(intervals)
        i = 0

        while k-1 > 0:
            curX, curY = intervals[i][0], intervals[i][1]
            nexX, nexY = intervals[i+1][0], intervals[i+1][1]

            if curX <= nexY and nexX <= curY:
                intervals.pop(i+1)
                intervals.insert(i,[min(curX,nexX),max(curY,nexY)])
                intervals.pop(i+1)
            else:
                i += 1
            k -= 1
        return intervals
