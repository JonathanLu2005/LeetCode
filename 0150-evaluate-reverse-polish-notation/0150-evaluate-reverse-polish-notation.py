class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set(["+", "-", "*", "/"])

        for x in tokens:
            if x in operations:
                v2 = stack.pop(-1)
                v1 = stack.pop(-1)

                if x == "+":
                    stack.append(v1+v2)
                elif x == "-":
                    stack.append(v1-v2)
                elif x == "/":
                    stack.append(int(v1/v2))
                elif x == "*":
                    stack.append(v1*v2)
            else:
                stack.append(int(x))
        return stack[0]