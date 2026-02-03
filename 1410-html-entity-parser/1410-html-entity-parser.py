class Solution:
    def entityParser(self, text: str) -> str:
        # take HTML code, replace speical character by the thing it self
        # we have a stack, and we itearte through text
        # and we keep appending the text into the stack
        # now if the text is one of teh special characters, we need to add that special character
        # otherwise, if its regular text, the moment we hit a space 
        # is the moment we just add the text
        hashmap = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }

        # lengths = 4 5 6 7
        text += " "

        result = ""
        stack = ""

        for x in text:
            stack += x
            n = len(stack)
            four = ""
            five = ""
            six = ""
            seven = ""
            if n >= 4:
                four = stack[-4:]
            if n >= 5:
                five = stack[-5:]
            if n >= 6:
                six = stack[-6:]
            if n >= 7:
                seven = stack[-7:]

            if x in hashmap:
                result += hashmap[stack]
                stack = ""
            elif four in hashmap:
                result += stack[:-4] + hashmap[four]
                stack = ""
            elif five in hashmap:
                result += stack[:-5] + hashmap[five]
                stack = ""
            elif six in hashmap:
                result += stack[:-6] + hashmap[six]
                stack = ""
            elif seven in hashmap:
                result += stack[:-7] + hashmap[seven]
                stack = ""

            if x == " ":
                result += stack
                stack = ""
        return result[:-1]

