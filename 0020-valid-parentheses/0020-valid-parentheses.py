class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        hashmap = { ")":"(", "]":"[", "}":"{"}

        stack = []

        s = list(s)

        for x in s:
            if x in hashmap:
                if len(stack) == 0:
                    return False
                elif stack.pop() == hashmap[x]:
                    pass
                else:
                    return False
            else:
                stack.append(x)

        return (len(stack) == 0)

        """
        same idea but just better execution

        stack = []
        hm = { ")":"(", "[":"]". "{":"}"}

        for c in s:
            if c in hm:
                if stack and stack[-1] == hm[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        """