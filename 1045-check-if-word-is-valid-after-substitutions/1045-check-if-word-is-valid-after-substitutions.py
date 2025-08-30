class Solution:
    def isValid(self, s: str) -> bool:
        # need to eliminate all of the abc
        # only remove iff there's abc
        stack = []

        for x in s:
            if x == 'c' and len(stack) > 1 and stack[-1] == 'b' and stack[-2] == 'a':
                stack.pop(-1)
                stack.pop(-1)
            else:
                stack.append(x)

        return (stack == [])