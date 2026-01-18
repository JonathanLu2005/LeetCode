class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        result = []

        candidates = list(set(candidates))
        n = len(candidates)

        def backtrack(index):
            if sum(subset) >= target or index == n:
                if sum(subset) == target:
                    result.append(subset[:])
                return

            subset.append(candidates[index])
            backtrack(index)

            subset.pop(-1)
            index += 1
            backtrack(index)
        backtrack(0)
        return result