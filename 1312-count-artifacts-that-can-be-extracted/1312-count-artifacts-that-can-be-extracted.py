class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        # r1, c1, r2, c2 = where ith artificat is in
        # r1 c1 top left, r2 c2 bottom right
        # go through cells, if has part of artificat, will be uncovered
        # if all are uncovered, extract artifcat
        # have 2d array which indicates whre i dig
        # for each artificat, get all the cells needed
        # then get all the dig cells
        # so artificat have set of cells, we've a set of dig cells
        # if we do difference and theres nothing, or interesect and its equal to artificat
        # then we've fully uncovered it
        hashmap = {}

        # get artifact cells
        for i in range(0, len(artifacts)):
            artifact = artifacts[i]
            r1, c1, r2, c2 = artifact[0], artifact[1], artifact[2], artifact[3]

            cells = set()
            for row in range(r1,r2+1):
                for col in range(c1,c2+1):
                    cells.add((row,col))
            hashmap[i] = cells

        # get cells we dig
        visited = set()

        for [r,c] in dig:
            visited.add((r,c))

        result = 0

        for key, value in hashmap.items():
            artifact = hashmap[key]

            uncovered = artifact.intersection(visited)

            if uncovered == artifact:
                result += 1

        return result

        