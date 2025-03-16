class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        # this is how can use stack to help backtrack and keep track
        # know "".join(list)

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res

        """
        current1 = "("
        res = []

        def backtrack(openCount, closeCount, current):
            if openCount == n and closeCount == n:
                res.append(current)
                return 

            temp = current

            if openCount <= n:
                current += "("
                backtrack(openCount + 1, closeCount, current)
                current = temp

            if closeCount < openCount:
                current += ")"
                backtrack(openCount, closeCount + 1, current)
                current = temp

            return

        backtrack(1,0, current1)
        return res"""