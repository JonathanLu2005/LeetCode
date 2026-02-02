class Solution:
    def simplifyPath(self, path: str) -> str:
        # given absolute path, put into simplified path
        # begin wtih /, . is current dir, .. is previous dir, multiple slahes are just 1
        # multiple / = 1
        # no / at end
        # ... or more is a name
        # if we have ., that just means we're in the current directory so redundant
        # if we have .., mean previous
        # and we dont want . or .., so just remove them ig
        names = []

        name = ""

        for x in path:
            if x == "/":
                if name != "":
                    if name == "..":
                        if names:
                            names.pop(-1)
                    elif name != ".":
                        names.append(name)
                    name = ""
            else:
                name += x

        if name != "":
            if name == "..":
                if names:
                    names.pop(-1)
            elif name != ".":
                names.append(name)

        if len(names) == 0:
            return "/"
        result = ""
        for x in names:
            result += "/" + x
        return result