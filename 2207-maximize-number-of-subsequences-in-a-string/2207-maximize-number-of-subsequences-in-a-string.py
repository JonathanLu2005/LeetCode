class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # waht if start == end
        # aaa
        # aa
        # a a
        #  aa
        # so first a work with everytihng forward
        # 2nd a work with everything forward
        # so n-1, n-2, n-3
        # n = 4
        # aaaa
        # a -> 3
        #  a -> 2
        #   a -> 1
        # (n-1)(n-2)
        start = pattern[0]
        end = pattern[1]
        stack = ""
        hashmap = {}

        for x in text:
            if x == start or x == end:
                hashmap[x] = hashmap.get(x,0) + 1
                stack += x

        if stack == "":
            return 0

        if start == end:
            value = hashmap[start]
            value += 1


            result = ((value-1) * (value)) / 2
            return int(result)

        if hashmap.get(start,0) > hashmap.get(end,0):
            stack += end
        else:
            stack = start + stack
        #print(stack)
        
        startCount = 0
        endCount = 0
        result = 0

        # if we go from end start end, we cant use that start on previous end, so we gotta cut it out
        # so if end > 0 and we go to start, then reset to 0
        # actually if we go to any start, reset end to 0

        for x in stack:
            if x == start:
                result += (startCount * endCount)
                startCount += 1
                endCount = 0
            elif x == end:
                endCount += 1

        result += (endCount * startCount)
        return result