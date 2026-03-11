class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        # letters, k
        # 2 euqual char = close => distance most k
        # right merge to left
        # continue until no more merges
        # return resulting string

        # conveyor belt => o(n)
        # window = array, easily pop and append, o(1)
        # hasmhap to keep track, if its inside hashmap, we merge, else we pop and remove from hashmap
        # set

        result = ""
        window = []
        letters = set()

        for x in s:
            if len(window) == k:
                if x not in letters:
                    letter = window.pop(0)
                    result += letter
                    letters.remove(letter)
                    window.append(x)
                    letters.add(x)
            else:
                if x not in letters:
                    letters.add(x)
                    window.append(x)

        result += "".join(window)
        return result

