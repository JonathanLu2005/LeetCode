class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # find total pair = n * n-1 / 2
        # then find each component
        # find how many have pair already n * n -1 /2
        # take away from total and voila

        total = (n * (n-1)) / 2
        hashmap = {}

        nodes = set()

        for x, y in edges:
            nodes.add(x)
            nodes.add(y)
            if x in hashmap:
                hashmap[x].add(y)
            else:
                hashmap[x] = set([y])

            if y in hashmap:
                hashmap[y].add(x)
            else:
                hashmap[y] = set([x])

        # then do dfs and see how long each components are
        visited = set()

        def dfs(node):
            stack = set([node])

            count = 0
            while stack:
                node = stack.pop()

                if node not in visited:
                    visited.add(node)
                    count += 1

                    stack.update(hashmap.get(node,set()))

            return count

        for node in nodes:
            if node not in visited:
                result = dfs(node)
                total -= ((result * (result - 1)) / 2)
 
        return int(total)


