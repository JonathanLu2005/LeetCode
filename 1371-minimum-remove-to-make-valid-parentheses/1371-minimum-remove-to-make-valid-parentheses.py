class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack
        # holds ()
        # more importantly hold [index, symbol]
        # if symbol ) then pop
        # then we'll have stack of indexes to remove
        stack = []

        for i in range(0, len(s)):
            symbol = s[i]

            if symbol == "(":
                stack.append([i, symbol])
            elif symbol == ")":
                if stack:
                    if stack[-1][1] == "(":
                        stack.pop()
                    else:
                        stack.append([i, symbol])
                else:
                    stack.append([i, symbol])

        if len(stack) == 0:
            return s

        indexes = set()

        for index, symbol in stack:
            indexes.add(index)  

        result = ""
        for i in range(0, len(s)):
            if i not in indexes:
                result += s[i]
        return result
