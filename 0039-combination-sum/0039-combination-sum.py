class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # can do backtracking, where we go through every node
        # we decide if we keep it or not, and we keep adding
        # moment we reach end of candidates, ok we stop and check if we have soemthing
        # otherwise moment we reach target we have something
        # otherwise moment we exceed target its not worth it
        result = []

        def backtrack(index,subset,total):
            if index == len(candidates) or total >= target:
                if total == target:
                    result.append(subset.copy())
                return

            # use
            subset.append(candidates[index])
            total += candidates[index]
            backtrack(index,subset,total)

            # not use
            subset.pop(-1)
            total -= candidates[index]
            index += 1
            backtrack(index,subset,total)

        backtrack(0,[],0)
        return result