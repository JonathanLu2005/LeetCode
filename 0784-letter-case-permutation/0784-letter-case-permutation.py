class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # bakctracking where we can keep going the thing
        # choose to lowercase or uppercase it

        result = []

        def backtrack(i,subset):
            if i == len(s):
                result.append(subset)
                return

            letter = s[i]
            if letter.isdigit():
                subset += letter
                i += 1
                backtrack(i,subset)
            else:
                i += 1
                backtrack(i,subset + letter.lower())
                backtrack(i,subset + letter.upper())
        backtrack(0,"")
        return result

            
