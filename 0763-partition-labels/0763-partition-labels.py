class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # partition s.t. each letter appear in most 1 part, so never again
        # do intervals?
        # for each letter, note when they first appear and last appear
        # and then through that we can merge intervals if overlap
        hashmap = {}
        n = len(s)

        for i in range(0,n):
            letter = s[i]

            if letter not in hashmap:
                hashmap[letter] = [i,i]
            hashmap[letter][1] = i

        intervals = sorted(hashmap.values())
        
        i = 0
        n = len(intervals)

        # [0,5]  [1,8]

        while i < n - 1:
            currentX = intervals[i][0]
            currentY = intervals[i][1]

            nextX = intervals[i+1][0]
            nextY = intervals[i+1][1]

            if nextX <= currentY:
                newX = min(nextX,currentX)
                newY = max(nextY,currentY)

                intervals.pop(i+1)
                intervals[i] = [newX,newY]
                n -= 1
            else:
                i += 1

        result = []
        for [x,y] in intervals:
            result.append(y-x+1)
        return result

        