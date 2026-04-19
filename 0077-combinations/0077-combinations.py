class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return all possible combo of k num
        # from range 1 to n
        # ah 
        # i mean at value 1, we should keep choosing if we want to keep vlaue or not
        # basically moving forwards, every value, decide if want to keep or not
        # and need to be k length, then we can find the potential combo
        result = []

        def backtrack(i,subset,length):
            if i == (n+1):
                if length == k:
                    result.append(subset.copy())
                return

            # keep
            length += 1
            subset.append(i)
            i += 1
            backtrack(i,subset,length)

            # no keep
            length -= 1
            subset.pop(-1)
            backtrack(i,subset,length)

        backtrack(1,[],0)
        return result
