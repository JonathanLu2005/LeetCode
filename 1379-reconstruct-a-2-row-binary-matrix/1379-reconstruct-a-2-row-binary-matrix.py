class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if lower + upper != sum(colsum):
            return []

        result = [[0 for x in range(0, len(colsum))] for x in range(0,2)]
        indices = set()
        for i in range(0, len(colsum)):
            if colsum[i] == 2:
                lower -= 1
                upper -= 1

                result[0][i] = 1
                result[1][i] = 1
            if colsum[i] == 1:
                indices.add(i)

        if upper < 0 or lower < 0:
            return []

        for i in indices:
            if upper > 0:
                result[0][i] = 1
                upper -= 1
            elif lower > 0:
                result[1][i] = 1
                lower -= 1
        
        return result
                