class Solution:
    def resultingString(self, s: str) -> str:
        # if have 2 consecutive letters
        # remvoe leftmost adjacent pair thats consecutive in alphabet
        # e.g a b, b a, and shift remaining char to fill gap
        # return once done
        # circular
        # get ascii values, if difference is 1 remove, else if 24 ish then remove
        # continue 

        stack = []

        for x in s:
            if len(stack) >= 1:
                t = ord(stack[-1])
                v = ord(x)
                res = abs(t-v)

                if res == 1 or res == 25:
                    stack.pop(-1)
                else:
                    stack.append(x)
            else:
                stack.append(x)

        return "".join(stack)
            
            