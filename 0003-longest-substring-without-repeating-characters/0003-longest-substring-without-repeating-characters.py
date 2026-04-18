class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring
        # so essentially, every character we pass through
        # we want to track it, and the moment something repeats, we stop, we store the current length
        # and we want to remove every character till we remove the duplicate, so we can start again
        # abcd b = 4
        # cdb
        # as we traverse, we could store this in a set, and we can store this in an array
        # and the moment we keep adding, the momenth the lengths are different, mean theres a duplicate
        # so we stop, we store the length, then we remove the duplicate and continue on
        unique = set()
        letters = []
        result = 0

        for x in s:
            letters.append(x)
            unique.add(x)

            if len(letters) != len(unique):
                result = max(result,len(unique))

                letter = letters.pop(0)
                unique.remove(letter)
                while letter != x:
                    letter = letters.pop(0)
                    unique.remove(letter)                    
                unique.add(x)

        result = max(result,len(unique))
        return result