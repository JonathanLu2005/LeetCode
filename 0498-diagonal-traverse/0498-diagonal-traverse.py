class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # add together as key
        # even order by big to small
        # odd order by small to big
        hashmap = {}

        for row in range(0,len(mat)):
            for col in range(0,len(mat[0])):
                key = row + col

                if key not in hashmap:
                    hashmap[key] = []
                hashmap[key].append(mat[row][col])

        res = []

        maxKey = len(mat) + len(mat[0]) - 1

        for key in range(0, maxKey):
            values = hashmap[key]

            if key % 2 == 0:
                values = values[::-1]

            res.extend(values)
        return res