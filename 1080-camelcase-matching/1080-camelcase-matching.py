class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # every letter need match the pattern else cooked
        # if encountered another capital afterwards then cooked
        # put lowercase anywhere aslong as it exists cool
        # jsut capital we care about
        result = []
        n = len(pattern)

        for word in queries:
            i = 0
            flag = True
            for c in word:
                if i < n:
                    if c == pattern[i]:
                        i += 1
                    elif c.isupper():
                        flag = False
                        break
                else:
                    if c.isupper():
                        flag = False
                        break
            if i != n:
                flag = False
            result.append(flag)
        return result
            