class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # basically we insert a new interval, and need merge it with toher intervals
        # hold the new start and end,
        # if interval doesnt intersect, then we chill and add it and continue
        # if it does, we update new start and new end
        # such that if next one need to merge, we merge it
        # else we add it
        # have a value to see if we added midway or need add at end
        # if add at end then add it at end
        if not intervals:
            return [newInterval]

        newStart, newEnd = newInterval[0], newInterval[1]
        result = []
        #start = False
        added = False

        #if newStart < intervals[0][0] and newEnd < intervals[0][0]:
        #    intervals.insert(0,[newStart,newEnd])
        #    return intervals

        for [x,y] in intervals:
            if newStart < x and newEnd < x:
                if not added:
                    result.append([newStart,newEnd])
                    added = True
                result.append([x,y])
            elif x <= newEnd and newStart <= y:
                #start = True
                newStart = min(x,newStart)
                newEnd = max(y,newEnd)
            else:
                result.append([x,y])

        if not added:
            result.append([newStart, newEnd])

        return result