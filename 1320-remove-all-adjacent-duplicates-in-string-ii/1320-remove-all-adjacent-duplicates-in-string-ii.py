class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # keep count for every character append to as a tuple
        # if hit k, remove it, else keep whatever and concatenate and return as result
        stack = []

        for x in s:
            if stack and stack[-1][0] == x:
                stack[-1] = (x, stack[-1][1] + 1)

                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append((x,1))

        return "".join(x * count for x, count in stack)

        """ original
        # stack
        # keep appending, check if last k is same, if so remove
        # then check again in case, if chill then its chill we can continue on
        stack = []

        for x in s:
            stack.append(x)

            if len(stack) >= k:
                if stack[-k:] == ([stack[-1]] * k):
                    stack = stack[:-k]

        return "".join(stack)
        """