class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
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