class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # find unique combo of candidates, where sum
        # only use once
        # no duplicate comboos
        # uhh store set of them in somewhere else for us to worry about
        result = set()
        candidates = sorted(candidates)

        def backtrack(index,subset,total):
            if index == len(candidates) or total >= target:
                if total == target:
                    result.add(tuple(subset.copy()))
                return 

            total += candidates[index]
            subset.append(candidates[index])
            index += 1
            backtrack(index,subset,total)

            total -= candidates[index-1]
            subset.pop(-1)
            backtrack(index,subset,total)

        backtrack(0,[],0)
        final = []

        for x in result:
            final.append(list(x))
        return final
            
